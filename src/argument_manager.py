"""
This module is designed to parse command-line arguments for the package comparison tool.
"""

import argparse


def parse_args():
    """
    Parses the command-line arguments.

    Returns:
        argparse.Namespace: object with the parsed command-line arguments.
        
    Function define and parse command-line arguments:
    - branch1: the name of the first branch for comparison.
    - branch2: the name of the second branch for comparison.
    - output: optional argument specifying the filename (without extension).
            Defaults to 'result', saving the file as 'result.json' in the current directory.
    """
    parser = argparse.ArgumentParser(description="Compares packages between two branches.")
    parser.add_argument("branch1", type=str, help="Name of the first branch")
    parser.add_argument("branch2", type=str, help="Name of the second branch")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="result",
        help='File name to save the results in the current directory.',
    )
    return parser.parse_args()