import enum


class AvailabilityStatus(enum.Enum):
    TLS = enum.auto()
    HTTP = enum.auto()
    OnlyPing = enum.auto()
    NoPing = enum.auto()
    Down = enum.auto()
    GAIFailed = enum.auto()

    Fallback = enum.auto()
