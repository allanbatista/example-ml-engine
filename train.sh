#!/usr/bin/env bash

echo "Submitting a Cloud ML Engine job..."

CURRENT_DATE=`date +%Y%m%d_%H%M%S`
MODEL_NAME="example_ml_engine"
EPOCHS=100

BASE_PATH="gs://eco-league-244218/tmp/$MODEL_NAME"
BUCKET_NAME=eco-league-244218
TRAIN_PATH="${BASE_PATH}/train/${CURRENT_DATE}"

JOB_NAME=${MODEL_NAME}_${CURRENT_DATE}
JOB_DIR="$TRAIN_PATH/job/"

gcloud ai-platform jobs submit training ${JOB_NAME} \
        --scale-tier=standard-1 \
        --job-dir=${JOB_DIR} \
        --runtime-version=1.14 \
        --python-version=3.5 \
        --region="us-west1" \
        --module-name=ml_engine.main \
        --package-path=ml_engine \
        -- \
        --job-name=${JOB_NAME}