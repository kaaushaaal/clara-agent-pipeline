import json
import sys
import os

account_id = sys.argv[1]


def generate_agent():

    with open(f"outputs/accounts/{account_id}/v1/memo.json") as f:
        memo = json.load(f)

    agent = {

        "agent_name": memo["company_name"] + " AI Receptionist",

        "voice_style": "professional calm",

        "version": "v1",

        "key_variables": {
            "company_name": memo.get("company_name"),
            "services": memo.get("services_supported", []),
            "business_hours": memo.get("business_hours", {}),
            "emergency_definition": memo.get("emergency_definition", [])
        },

        "call_transfer_protocol": {
            "primary": "dispatch",
            "timeout_seconds": 60
        },

        "fallback_protocol": {
            "message": "We could not reach dispatch. A technician will call you shortly."
        },

        "system_prompt": f"""
You are an AI receptionist for {memo.get("company_name")}.

Your job is to answer calls, collect key information, and route the caller appropriately.

BUSINESS HOURS FLOW

1. greet the caller politely
2. ask the purpose of the call
3. collect caller name and phone number
4. determine service request
5. transfer the call to the appropriate person if necessary
6. if transfer fails, apologize and explain that someone will follow up shortly
7. confirm next steps
8. ask if they need anything else
9. close the call politely

AFTER HOURS FLOW

1. greet the caller
2. ask the purpose of the call
3. determine whether the situation is an emergency

If emergency:
- collect caller name
- collect phone number
- collect service address immediately
- attempt transfer to on-call technician

If transfer fails:
- apologize and assure the caller someone will follow up shortly

If non-emergency:
- collect caller details
- inform the caller someone will follow up during business hours

Finally:
- ask if they need anything else
- close the call politely
"""
    }

    os.makedirs(f"outputs/accounts/{account_id}/v1", exist_ok=True)

    with open(f"outputs/accounts/{account_id}/v1/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)

    print("agent_spec_v1.json created")


if __name__ == "__main__":
    generate_agent()