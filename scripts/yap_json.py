from modules import scripts, script_callbacks
import json
import os

PRESET_FILE = os.path.join(scripts.basedir(), "presets.json")


def load_presets():
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

    print(elem_ids)


script_callbacks.on_before_ui(load_presets)
