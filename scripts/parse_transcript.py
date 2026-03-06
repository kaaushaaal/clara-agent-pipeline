def parse_transcript(file_path):

    with open(file_path, "r") as f:
        text = f.read().lower()

    services = []

    keywords = [
        "ev charger",
        "hot tub",
        "panel",
        "outlet",
        "troubleshooting",
        "renovation",
        "tenant"
    ]

    for k in keywords:
        if k in text:
            services.append(k)

    integrations = []
    if "jobber" in text:
        integrations.append("Jobber CRM")

    return {
        "services_supported": services,
        "integration_constraints": integrations,
        "questions_or_unknowns": [
            "exact business hours",
            "timezone",
            "transfer timeout rules"
        ]
    }