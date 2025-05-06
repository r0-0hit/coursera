def make_sandwich(
    bread_type: str, filling: str, cheese: str = "none", toasted: bool = False
) -> str:
    description = "Making a "

    if toasted:
        description += "toasted "

    description += f"{bread_type} sandwich with {filling}"

    if cheese.lower() != "none":
        description += f" and {cheese} cheese"

    description += "."

    return description


print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))
