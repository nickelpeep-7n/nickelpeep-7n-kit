"""Command line entry point for nickelpeep_7n_kit."""
import argparse

from .core import Nickelpeep7nTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="csv numeric summary")
    parser.add_argument("path")
    parser.add_argument("--column")
    args = parser.parse_args(argv)
    for name, stats in Nickelpeep7nTool().summarize(args.path, args.column).items():
        print(f"{name}: n={stats['n']} min={stats['min']} max={stats['max']} mean={stats['mean']}")
    return 0
