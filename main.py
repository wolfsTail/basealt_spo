#!/usr/bin/env python3

import sys

from src.argument_manager import parse_args
from src.comparator import PackagesComparer
from src.parsers import PackagesFetcher
from src.writer import save_results


def main():
    args = parse_args()

    branch1_packages = PackagesFetcher.get_binary_packages(args.branch1)
    branch2_packages = PackagesFetcher.get_binary_packages(args.branch2)

    compare_result = PackagesComparer.compare_packages(
        args.branch1, branch1_packages, args.branch2, branch2_packages
    )
    save_results(f"{args.output}.json", compare_result)


if __name__ == "__main__":
    main()
