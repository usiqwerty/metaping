from argparse import ArgumentParser

from metaping.scan import batch_scan

argparser = ArgumentParser()
argparser.add_argument("hosts", nargs="+")


def run_cli():
    print("metaping 0.1")
    args = argparser.parse_args()
    batch_scan(args.hosts)
