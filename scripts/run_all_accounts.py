import os
import subprocess
import sys

DATASET_PATH = "dataset"

if not os.path.exists(DATASET_PATH):
    print("Dataset folder not found")
    sys.exit(1)

accounts = os.listdir(DATASET_PATH)

for account in accounts:

    account_path = os.path.join(DATASET_PATH, account)

    if not os.path.isdir(account_path):
        continue

    print("\nProcessing account:", account)

    subprocess.run([
        sys.executable,
        "scripts/run_pipeline.py",
        account
    ])