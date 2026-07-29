"""CLI entrypoint for the elis-slr package.

Usage:
    elis-slr --help
    elis-slr version
    elis-slr <subcommand> [options]
"""

import argparse
import sys

from elis_slr import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the elis-slr CLI."""
    parser = argparse.ArgumentParser(
        prog="elis-slr",
        description="Systematic Literature Review (SLR) protocol CLI",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"elis-slr {__version__}",
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    # version subcommand (explicit)
    version_parser = subparsers.add_parser("version", help="Show version")
    version_parser.set_defaults(func=_cmd_version)

    return parser


def _cmd_version(args: argparse.Namespace) -> None:
    """Print version and exit."""
    print(f"elis-slr {__version__}")


def main(argv: list[str] | None = None) -> int:
    """Main entrypoint for the elis-slr CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if hasattr(args, "func"):
        args.func(args)

    return 0


if __name__ == "__main__":
    sys.exit(main())