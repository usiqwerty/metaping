import ctypes
import os
import socket
import time


def __ping_windows(host: str, timeout: int = 1000) -> float | None:
    icmp = ctypes.windll.iphlpapi.IcmpSendEcho
    handle = ctypes.windll.iphlpapi.IcmpCreateFile()

    addr = socket.gethostbyname(host)
    send_data = b"abcdefghijklmnopqrstuvwabcdefghi"  # 32 bytes
    recv_buffer = ctypes.create_string_buffer(1024)

    start = time.time()
    result = icmp(
        handle,
        socket.inet_aton(addr),
        send_data,
        len(send_data),
        None,
        recv_buffer,
        ctypes.sizeof(recv_buffer),
        timeout
    )

    if result == 0:
        return None  # no reply

    time_sent = time.time()
    rtt = (time_sent - start) * 1000
    return rtt


def ping(host: str, timeout: int = 1000):
    if os.name == 'nt':
        return __ping_windows(host, timeout)
    raise NotImplementedError
