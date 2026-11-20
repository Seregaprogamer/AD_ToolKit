---
aliases:
  - "Включённые зависимости · Linux amd64"
tags:
  - ad
  - установка
---

# Включённые зависимости · Linux amd64

Имена библиотек соответствуют SONAME из фактической сборки. Собственные обёртки передают загрузчику приватный каталог lib. Список нужен, чтобы диагностировать ошибку загрузки.

| Файл | Прямые зависимости ELF |
|---|---|
| rg | статический ELF |
| curl | libcurl.so.4, libz.so.1, libc.so.6 |
| jq | libjq.so.1, libc.so.6 |
| libbrotlicommon.so.1 | libc.so.6 |
| libbrotlidec.so.1 | libbrotlicommon.so.1, libc.so.6 |
| libcom_err.so.2 | libc.so.6, ld-linux-x86-64.so.2 |
| libcrypto.so.3 | libz.so.1, libzstd.so.1, libc.so.6 |
| libcurl.so.4 | libnghttp3.so.9, libnghttp2.so.14, libidn2.so.0, librtmp.so.1, libssh2.so.1, libpsl.so.5, libssl.so.3, libcrypto.so.3, libgssapi_krb5.so.2, libldap.so.2, liblber.so.2, libzstd.so.1, libbrotlidec.so.1, libz.so.1, libc.so.6 |
| libffi.so.8 | libc.so.6 |
| libgmp.so.10 | libc.so.6 |
| libgnutls.so.30 | libp11-kit.so.0, libidn2.so.0, libunistring.so.5, libtasn1.so.6, libhogweed.so.6, libnettle.so.8, libgmp.so.10, libc.so.6, ld-linux-x86-64.so.2 |
| libgssapi_krb5.so.2 | libkrb5.so.3, libk5crypto.so.3, libcom_err.so.2, libkrb5support.so.0, libc.so.6 |
| libhogweed.so.6 | libnettle.so.8, libgmp.so.10, libc.so.6 |
| libidn2.so.0 | libunistring.so.5, libc.so.6 |
| libjq.so.1 | libm.so.6, libonig.so.5, libc.so.6, ld-linux-x86-64.so.2 |
| libk5crypto.so.3 | libkrb5support.so.0, libc.so.6 |
| libkeyutils.so.1 | libc.so.6 |
| libkrb5.so.3 | libk5crypto.so.3, libcom_err.so.2, libkrb5support.so.0, libkeyutils.so.1, libresolv.so.2, libc.so.6 |
| libkrb5support.so.0 | libc.so.6 |
| liblber.so.2 | libc.so.6 |
| libldap.so.2 | liblber.so.2, libsasl2.so.2, libssl.so.3, libcrypto.so.3, libc.so.6 |
| libnettle.so.8 | libc.so.6 |
| libnghttp2.so.14 | libc.so.6 |
| libnghttp3.so.9 | libc.so.6 |
| libonig.so.5 | libc.so.6 |
| libp11-kit.so.0 | libffi.so.8, libc.so.6, ld-linux-x86-64.so.2 |
| libpsl.so.5 | libunistring.so.5, libidn2.so.0, libc.so.6 |
| librtmp.so.1 | libgnutls.so.30, libhogweed.so.6, libnettle.so.8, libgmp.so.10, libz.so.1, libc.so.6 |
| libsasl2.so.2 | libcrypto.so.3, libc.so.6 |
| libssh2.so.1 | libcrypto.so.3, libz.so.1, libc.so.6 |
| libssl.so.3 | libcrypto.so.3, libc.so.6 |
| libtasn1.so.6 | libc.so.6 |
| libunistring.so.5 | libc.so.6 |
| libz.so.1 | libc.so.6 |
| libzstd.so.1 | libc.so.6 |

[[START_HERE|На главную]]
