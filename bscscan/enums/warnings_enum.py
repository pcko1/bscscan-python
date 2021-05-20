from dataclasses import dataclass


@dataclass(frozen=True)
class WarningsEnum:
    DEPRECATION_WARNING: str = "This class is deprecated."