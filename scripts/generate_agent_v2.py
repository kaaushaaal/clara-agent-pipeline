import json
import os
import sys

account_id = sys.argv[1]


def generate_agent_v2():

    with open(f"outputs/accounts/{account_id}/v2/memo.json", "r") as f:
        memo = json.load(f)

    agent = {

        "agent_name": memo["company_name"] + " AI Receptionist",

        "version": "v2",

        "voice_style": "professional",

        "variables": {
            "company_name": memo.get("company_name"),
            "services": memo.get("services_supported", []),
            "business_hours": memo.get("business_hours"),
            "office_address": memo.get("office_address"),
            "emergency_definition": memo.get("emergency_definition", [])
        },

        "transfer_protocol": {
            "timeout_seconds": 60,
            "retry_attempts": 1,
            "fallback": "inform caller someone will follow up shortly"
        },

        "system_prompt": f"""
You are an AI receptionist for {memo.get("company_name")}.

Your role is to answer incoming calls, collect essential information,
and route the caller appropriately.

BUSINESS HOURS CALL FLOW

1. Greet the caller politely.
2. Ask the reason for the call.
3. Collect the caller's name and phone number.
4. Determine whether the request relates to:
   - emergency service
   - non-emergency service
5. If appropriate, transfer the call to the correct technician or department.
6. If transfer fails:
   - apologize
   - inform the caller that someone will follow up shortly.
7. Confirm the next steps with the caller.
8. Ask if they need anything else.
9. Close the call politely.

AFTER HOURS CALL FLOW

1. Greet the caller.
2. Ask the purpose of the call.
3. Determine whether the situation is an emergency.

If emergency:
- collect caller name
- collect phone number
- collect service address immediately
- attempt transfer to the on-call technician.

If transfer fails:
- apologize
- assure the caller someone will respond as soon as possible.

If non-emergency:
- collect caller information
- inform the caller that someone will follow up during business hours.

Finally:
- ask if they need anything else
- close the call politely.
"""
    }

    os.makedirs(f"outputs/accounts/{account_id}/v2", exist_ok=True)

    with open(f"outputs/accounts/{account_id}/v2/agent_spec.json", "w") as f:
        json.dump(agent, f, indent=2)

    print("agent_spec_v2.json created")


if __name__ == "__main__":
    generate_agent_v2()