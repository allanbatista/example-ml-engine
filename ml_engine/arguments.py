import argparse


def build():
    ap = argparse.ArgumentParser()

    ap.add_argument(
        '--job-dir',
        help='jobs staging path on google cloud storage',
        required=True
    )

    ap.add_argument(
        '--job-name',
        help='set job name',
        required=True
    )

    return ap.parse_args()

