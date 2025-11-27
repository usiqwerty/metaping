from typing import Iterable, Callable

from metaping.astatus import AvailabilityStatus
from metaping.checkers.http import scan_http_s
from metaping.checkers.icmp import scan_ping


def __try_all_methods(funcs: Iterable[Callable], host: str) -> AvailabilityStatus:
    for func in funcs:
        st = func(host)
        if st != AvailabilityStatus.Fallback:
            return st


def scan_host(host: str) -> AvailabilityStatus:
    methods = [
        lambda d: scan_http_s(f"https://{d}/"),
        lambda d: scan_http_s(f"http://{d}/"),
        scan_ping,
        lambda x: AvailabilityStatus.Down,
    ]
    return __try_all_methods(methods, host=host)


def batch_scan(hosts: list[str]):
    for host in hosts:
        domain_status = scan_host(host)
        print(f"{host} [{domain_status.name}]")
