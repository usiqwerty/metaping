import http.client
import socket
import ssl
import urllib.error
import urllib.request

from metaping.astatus import AvailabilityStatus


def scan_http_s(url: str, timeout: int = 3) -> AvailabilityStatus:
    try:
        try:
            with urllib.request.urlopen(url, timeout=timeout) as u:
                u: http.client.HTTPResponse
                u.read()
        except urllib.error.HTTPError:
            pass
        if url.startswith("https://"):
            return AvailabilityStatus.TLS
        elif url.startswith("http://"):
            return AvailabilityStatus.HTTP

        raise ValueError(f"unknown scheme in url: {url}")

    except urllib.error.URLError as e:
        if isinstance(e.reason, ConnectionRefusedError):
            return AvailabilityStatus.Down
        elif isinstance(e.reason, TimeoutError):
            return AvailabilityStatus.Fallback
        elif isinstance(e.reason, socket.gaierror):
            return AvailabilityStatus.GAIFailed
        elif isinstance(e.reason, ssl.SSLError):
            return AvailabilityStatus.Fallback
        raise e
    except TimeoutError:
        return AvailabilityStatus.Fallback
