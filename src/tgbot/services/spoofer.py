import random

from settings.settings import SPOOFER_SETTINGS


def generate(text: str, level: int = 1) -> str:
    result = ""
    for counter, letter in enumerate(text, start=1):
        if (
            (counter == 1) or
            ((counter % SPOOFER_SETTINGS["extra_addresses"]) < level and
             counter != 1)
        ):
            result += random.choice(SPOOFER_SETTINGS['alph'].get(
                letter.lower(), (letter.lower(),))
            )
        else:
            result += letter
    return result


def generate_spoofing_addresses(original_address: dict):
    title_fields = ["name"]
    generate_fields = ["name", "street"]
    must_be_splited = ["name"]
    prefix_fields = ["house", "apartments", "street"]

    result = []
    for level in range(SPOOFER_SETTINGS["extra_addresses"]):
        new_obj = {}
        new_obj.update(original_address)
        for field in generate_fields:
            if field in must_be_splited:
                new_obj.update({field: " ".join(map(
                    lambda word: generate(word, level),
                    original_address[field].split()
                ))})
            else:
                new_obj.update({field: generate(original_address[field], level)})
        result.append(new_obj)

    new_result = []
    for address in result:
        # add prefixes for certain fields
        for field in prefix_fields:
            address[field] = (
                f"{random.choice(SPOOFER_SETTINGS[field])} "
                f"{address[field]}").strip()
        # format title for certain fields
        for field in title_fields:
            address[field] = address[field].title()

        new_result.append(address)
    return result
