"""NWA launcher.

Runs the original checker from dsv.py while presenting the renamed NWA branding.
The original source and license remain in dsv.py; please retain the original
author's credits when redistributing this fork.
"""
from pathlib import Path


OLD_BANNER = """  ██████╗ ███████╗██╗   ██╗
  ██╔══██╗██╔════╝██║   ██║
  ██║  ██║███████╗██║   ██║
  ██║  ██║╚════██║╚██╗ ██╔╝
  ██████╔╝███████║ ╚████╔╝
  ╚═════╝ ╚══════╝  ╚═══╝"""

NEW_BANNER = """  ███╗   ██╗██╗    ██╗ █████╗
  ████╗  ██║██║    ██║██╔══██╗
  ██╔██╗ ██║██║ █╗ ██║███████║
  ██║╚██╗██║██║███╗██║██╔══██║
  ██║ ╚████║╚███╔███╔╝██║  ██║
  ╚═╝  ╚═══╝ ╚══╝╚══╝ ╚═╝  ╚═╝"""


def main() -> None:
    source_path = Path(__file__).with_name("dsv.py")
    source = source_path.read_text(encoding="utf-8")
    # Apply the fork's branding at runtime without modifying the original file.
    source = source.replace("DSV", "NWA").replace("dsv.py", "nwa.py")
    # Replace the large DSV ASCII banner with an NWA banner.
    source = source.replace(OLD_BANNER, NEW_BANNER)
    namespace = {"__name__": "__main__", "__file__": str(source_path)}
    exec(compile(source, str(source_path), "exec"), namespace, namespace)


if __name__ == "__main__":
    main()
