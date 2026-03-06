import json
import os
from extract_onboarding_updates import extract_updates
import sys
account_id = sys.argv[1]

def update_memo():

    with open("outputs/accounts/bens-electric/v1/memo.json") as f:
        memo_v1 = json.load(f)

    updates = extract_updates(
        "dataset/bens-electric/onboarding_transcript.txt"
    )

    memo_v2 = memo_v1.copy()

    for key, value in updates.items():
        memo_v2[key] = value

    os.makedirs("outputs/accounts/bens-electric/v2", exist_ok=True)

    with open("outputs/accounts/bens-electric/v2/memo.json", "w") as f:
        json.dump(memo_v2, f, indent=2)

    return memo_v1, memo_v2


if __name__ == "__main__":
    v1, v2 = update_memo()
    print("memo_v2 created")