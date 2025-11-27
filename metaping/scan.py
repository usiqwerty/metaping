from metaping.astatus import AvailabilityStatus
from metaping.http_checker import scan_http_s
from metaping.ping_checker import ping_status


def _try_all_methods(*funcs, domain: str) -> AvailabilityStatus:
    for func in funcs:
        st = func(domain)
        if st != AvailabilityStatus.Fallback:
            return st


def scan_host(domain: str) -> AvailabilityStatus:
    return _try_all_methods(
        lambda d: scan_http_s(f"https://{d}/"),
        lambda d: scan_http_s(f"http://{d}/"),
        ping_status,
        lambda x: AvailabilityStatus.Down,
        domain=domain
    )


def batch_scan(domains: list[str]):
    for d in domains:
        domain_status = scan_host(d)
        print(f"{d} [{domain_status.name}]")
