from metaping.astatus import AvailabilityStatus
from metaping.ping import ping


def scan_ping(host: str):
    r = ping(host)
    if r is None:
        return AvailabilityStatus.Fallback
    return AvailabilityStatus.OnlyPing
