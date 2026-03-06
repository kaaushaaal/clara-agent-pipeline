def parse_onboarding(file_path):

    with open(file_path, "r") as f:
        text = f.read().lower()

    updates = {}

    if "business hours" in text:
        updates["business_hours"] = "extracted_from_onboarding"

    if "emergency" in text:
        updates["emergency_definition"] = ["emergency electrical issues"]

    return updates