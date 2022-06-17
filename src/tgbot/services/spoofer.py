import random

from settings.settings import SPOOFER_SETTINGS


def generate(text: str) -> str:
    result = ""
    for letter in text:
        result += random.choice(SPOOFER_SETTINGS['alph'].get(letter.lower(), (letter.lower(),)))
    return result


def generate_spoofing_addresses(original_address: dict):
    generate_fields = ["name", "street"]
    must_be_splited = ["name"]
    prefix_fields = ["house", "apartments", "street"]

    result = []
    for _ in range(SPOOFER_SETTINGS["extra_addresses"]):
        new_obj = {}
        new_obj.update(original_address)
        for field in generate_fields:
            if field in must_be_splited:
                new_obj.update({field: " ".join(map(generate, original_address[field].split()))})
            else:
                new_obj.update({field: generate(original_address[field])})
        result.append(new_obj)

    new_result = []
    for address in result:
        for field in prefix_fields:
            address[field] = (
                f"{random.choice(SPOOFER_SETTINGS[field])} "
                f"{address[field]}").strip()
        new_result.append(address)
    return result
