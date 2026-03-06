import sys
import json
import os

from parse_chat import parse_chat
from parse_transcript import parse_transcript

account_id = sys.argv[1]


def generate_memo():

    chat_data = parse_chat(f"dataset/{account_id}/chat.txt")
    transcript_data = parse_transcript(f"dataset/{account_id}/transcript.txt")

    memo = {

        "account_id": account_id,
        "company_name": "Ben's Electric Solutions",

        "contact_info": {
            "email": chat_data["email"],
            "phone": chat_data["phone"]
        },

        "services_supported": transcript_data["services_supported"],

        "integration_constraints": transcript_data["integration_constraints"],

        "business_hours": None,
        "office_address": None,

        "emergency_definition": [],
        "emergency_routing_rules": {},
        "non_emergency_routing_rules": {},

        "call_transfer_rules": {},

        "after_hours_flow_summary": None,
        "office_hours_flow_summary": None,

        "questions_or_unknowns": transcript_data["questions_or_unknowns"],

        "notes": "generated from demo call transcript"
    }

    return memo


def save_memo(memo):

    path = f"outputs/accounts/{account_id}/v1"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/memo.json", "w") as f:
        json.dump(memo, f, indent=2)


if __name__ == "__main__":

    memo = generate_memo()
    save_memo(memo)

    print("memo_v1.json created")