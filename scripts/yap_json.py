from modules import scripts
import json
import os

SAMPLE_FILE = os.path.join(scripts.basedir(), "example.json")
PRESET_FILE = os.path.join(scripts.basedir(), "presets.json")


def load_presets() -> tuple[dict, dict, list[str]]:

    if not os.path.isfile(PRESET_FILE):
        print('\n[Yapping]: Initializing "presets.json"...\n')
        os.rename(SAMPLE_FILE, PRESET_FILE)

    with open(PRESET_FILE, "r", encoding="utf-8") as preset:
        DATA: dict = json.load(preset)

    elem_ids = set()

    t2i: dict[str, dict] = DATA.get("txt2img", {})
    for configs in t2i.values():
        for elem in configs.keys():
            elem_ids.add(elem)

    i2i: dict[str, dict] = DATA.get("img2img", {})
    for configs in i2i.values():
        for elem in configs.keys():
            elem_ids.add(elem)

    return t2i, i2i, elem_ids
