import socket


def is_tcp_open(host: str, port: int, timeout: int = 5) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)

    try:
        is_open = s.connect_ex((host, int(port))) == 0 # True if open, False if not

        if is_open:
            s.shutdown(socket.SHUT_RDWR)

    except socket.error as er:
        is_open = False

    s.close()

    return is_open
