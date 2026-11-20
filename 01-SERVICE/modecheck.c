#include <stdio.h>
#include <string.h>

/* Маленькая программа с символами для исследования обычной ошибки конфигурации. */
static int check_mode(const char *mode) {
    if (strcmp(mode, "ready") == 0) return 0;
    if (strcmp(mode, "maintenance") == 0) return 2;
    return 3;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fputs("usage: modecheck ready|maintenance\n", stderr);
        return 1;
    }
    int result = check_mode(argv[1]);
    puts(result == 0 ? "ready" : "not ready");
    return result;
}
