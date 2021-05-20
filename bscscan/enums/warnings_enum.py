from dataclasses import dataclass


@dataclass(frozen=True)
class WarningsEnum:
    DEPRECATION_WARNING: str = (
        f"\n\nThis class is deprecated. It will SOON be removed."
        f"\n\nCheck https://github.com/pcko1/bscscan-python for more details.\n"
    )
    CONTEXT_MANAGER_WARNING: str = (
        f"\n\nThis class has been reformatted and now ONLY works within a context manager."
        f"\n\nCheck https://github.com/pcko1/bscscan-python for more details.\n"
    )