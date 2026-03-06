import re


def extract_updates(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()

    updates = {}

    # business hours
    hours_match = re.search(r'(\d{1,2}\s?(am|pm))\s?to\s?(\d{1,2}\s?(am|pm))', text)
    if hours_match:
        updates["business_hours"] = {
            "start": hours_match.group(1),
            "end": hours_match.group(3)
        }

    # emergency definition
    if "emergency" in text:
        updates["emergency_definition"] = [
            "critical electrical failure",
            "urgent service request"
        ]

    # transfer timeout
    timeout_match = re.search(r'(\d+)\s?seconds', text)
    if timeout_match:
        updates["call_transfer_rules"] = {
            "timeout_seconds": int(timeout_match.group(1))
        }

    # integrations
    if "jobber" in text:
        updates["integration_constraints"] = ["Jobber CRM"]

    return updates