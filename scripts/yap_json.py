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
    for btn, configs in t2i.items():
        for elem in configs.keys():
            elem_ids.add(elem)

            if "img2img" in elem:
                print(
                    f'\n[Yapping]: img2img component "{elem}" found in txt2img preset "{btn}"...?\n'
                )

    i2i: dict[str, dict] = DATA.get("img2img", {})
    for btn, configs in i2i.items():
        for elem in configs.keys():
            elem_ids.add(elem)

            if "txt2img" in elem:
                print(
                    f'\n[Yapping]: txt2img component "{elem}" found in img2img preset "{btn}"...?\n'
                )

    return t2i, i2i, elem_ids
