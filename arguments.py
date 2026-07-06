from argparse import ArgumentParser, Namespace
from functools import lru_cache
from typing import Sequence


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Reading Userbank and Job")
    parser.add_argument(
        "--bank_nr",
        dest="bank_nr",
        type=str,
        default=None,
        help="Userbank number",
    )
    parser.add_argument(
        "--job_nr",
        dest="job_nr",
        type=str,
        default=None,
        help="Job number",
    )
    return parser


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    return build_parser().parse_args(argv)


@lru_cache(maxsize=1)
def get_args() -> Namespace:
    # Parse only once so all imports share the same values.
    return parse_args()