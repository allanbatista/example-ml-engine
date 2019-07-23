import os
from datetime import datetime as dt

from ml_engine.arguments import build
from ml_engine.model import build_model

import tensorflow as tf


# Set python level verbosity
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.DEBUG)

# Set C++ Graph Execution level verbosity
os.environ['TF_CPP_MIN_LOG_LEVEL'] = str(tf.compat.v1.logging.DEBUG)


def main():
    model, score = build_model()

    print('Test loss:', score[0])
    print('Test accuracy:', score[1])


if __name__ == '__main__':
    arguments = build()
    time_start = dt.utcnow()
    print("[{}] Experiment started at {}".format(arguments.job_name, time_start.strftime("%H:%M:%S")))
    print(".......................................")

    main()

    time_end = dt.utcnow()
    time_elapsed = time_end - time_start
    print(".......................................")
    print("[{}] Experiment finished at {} / elapsed time {}s".format(arguments.job_name, time_end.strftime("%H:%M:%S"), time_elapsed.total_seconds()))