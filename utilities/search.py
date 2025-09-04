import re
from utilities.utils import WAREHOUSE_FILES 

INVENTORY: list[str] = [
    "Scanfrost Iron (1200W)",
    "LG Smart TV (32inch)",
    "Samsung Microwave (20L)",
    "Binatone Electric Kettle (1.8L)",
    "LG Smart TV (16inch)",
    "Philips Blender (1.5L)",
    "Haier Thermocool Refrigerator (165L)",
    "Samsung Microwave (20L)",
    "Tecno Spark 10 (128GB)",
    "Oraimo Powerbank (20000mAh)",
]


def reg_inspect(regex_list: list[re.Pattern[str]], item: str) -> bool:
    for reg in regex_list:
        a_match = re.search(reg, item)
        if a_match is None:
            return False
    return True


def search() -> list[str]:
    query: str = input("Search for an item from the store: ").strip()
    words: list[str] = query.split()
    regex: list[re.Pattern[str]] = []
    output: list[str] = []
    for word in words:
        reg: re.Pattern[str] = re.compile(re.escape(word), re.IGNORECASE)
        regex.append(reg)
    for item in WAREHOUSE_FILES:
        if reg_inspect(regex, item):
            output.append(item)
    return output


search_items: list[str] = search()
for item in search_items:
    i = search_items.index(item)
    print(f"{i+1}. {item}")
        