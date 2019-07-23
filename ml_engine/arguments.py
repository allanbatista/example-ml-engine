import argparse


class Arguments:
    def __init__(self, params):
        self.params = params

    @property
    def job_id(self):
        return self.params.job_dir

    @staticmethod
    def build():
        ap = argparse.ArgumentParser()

        ap.add_argument(
            '--job-dir',
            help='jobs staging path on google cloud storage',
            required=True
        )

        return Arguments(ap.parse_args())

