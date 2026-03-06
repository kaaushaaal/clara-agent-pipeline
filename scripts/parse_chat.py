import re

def parse_chat(file_path):

    result = {
        "email": None,
        "phone": None,
        "names": [],
        "companies": []
    }

    with open(file_path, "r") as f:
        text = f.read()

    emails = re.findall(r'\S+@\S+', text)
    phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)

    if emails:
        result["email"] = emails[0]

    if phones:
        result["phone"] = phones[0]

    return result