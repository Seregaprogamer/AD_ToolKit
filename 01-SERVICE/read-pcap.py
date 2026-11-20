"""Выводит стартовые строки HTTP из локального Ethernet/IPv4/TCP .pcap (без reassembly)."""
import argparse
import ipaddress
import struct
import sys

def show(stream):
    magic = stream.read(4)
    order = {bytes.fromhex("d4c3b2a1"): "<", bytes.fromhex("a1b2c3d4"): ">",
             bytes.fromhex("4d3cb2a1"): "<", bytes.fromhex("a1b23c4d"): ">"}.get(magic)
    if not order:
        raise ValueError("Ожидался классический PCAP, не pcapng")
    header = stream.read(20)
    if len(header) != 20 or struct.unpack(order + "I", header[-4:])[0] != 1:
        raise ValueError("Поддерживается только Ethernet PCAP")
    number = 0
    hits = 0
    while record := stream.read(16):
        number += 1
        if len(record) != 16:
            raise ValueError("Оборван заголовок кадра")
        size = struct.unpack(order + "4I", record)[2]
        if size > 16 * 1024 * 1024:
            raise ValueError("Слишком большой кадр")
        pkt = stream.read(size)
        if len(pkt) != size:
            raise ValueError("Оборван кадр")
        if len(pkt) < 54 or pkt[12:14] != b"\x08\x00" or pkt[23] != 6:
            continue
        start = 14 + (pkt[14] & 15) * 4
        if pkt[14] >> 4 != 4 or start < 34 or start + 20 > len(pkt):
            continue
        if int.from_bytes(pkt[20:22], "big") & 0x3fff:
            continue
        end = 14 + int.from_bytes(pkt[16:18], "big")
        header_size = (pkt[start+12] >> 4) * 4
        if header_size < 20 or end > len(pkt):
            continue
        data = pkt[start+header_size:end]
        line = data.split(b"\r\n", 1)[0][:240]
        if not line.startswith((b"GET ", b"POST ", b"HTTP/")):
            continue
        src, dst = map(ipaddress.IPv4Address, (pkt[26:30], pkt[30:34]))
        ports = struct.unpack("!HH", pkt[start:start+4])
        # Escape control characters from untrusted input before terminal display.
        print(f"{number:4} {src}:{ports[0]} -> {dst}:{ports[1]}  {ascii(line.decode('ascii','replace'))}")
        hits += 1
    print(f"Кадров: {number}; стартовых строк HTTP: {hits}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pcap")
    args = parser.parse_args()
    try:
        with open(args.pcap, "rb") as stream:
            show(stream)
    except (ValueError, OSError) as error:
        sys.exit(str(error))
