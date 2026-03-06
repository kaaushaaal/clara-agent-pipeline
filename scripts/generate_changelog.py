import json
import sys
account_id = sys.argv[1]

def generate_changelog():

    with open(f"outputs/accounts/{account_id}/v1/memo.json") as f:
        v1 = json.load(f)

    with open(f"outputs/accounts/{account_id}/v2/memo.json") as f:
        v2 = json.load(f)

    changes = []

    for key in v2:
        if v1.get(key) != v2.get(key):
            changes.append(key)

    with open(f"changelog/{account_id}.md", "w") as f:
        for c in changes:
            f.write(f"- {c} updated\n")

    print("changelog created")


if __name__ == "__main__":
    generate_changelog()