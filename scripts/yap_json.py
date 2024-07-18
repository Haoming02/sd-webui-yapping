from modules import scripts
import json
import os

SAMPLE_FILE = os.path.join(scripts.basedir(), "example.json")
PRESET_FILE = os.path.join(scripts.basedir(), "presets.json")

DATA: dict = None


def load_init():
    if not os.path.isfile(PRESET_FILE):
        print('\n[Yapping]: Initializing "presets.json"...\n')
        os.rename(SAMPLE_FILE, PRESET_FILE)

    global DATA
    with open(PRESET_FILE, "r", encoding="utf-8") as preset:
        DATA = json.load(preset)


def load_presets() -> tuple[dict, dict, set[str]]:
    elem_ids = set()

    t2i: dict[str, dict] = DATA.get("txt2img", {})
    for btn, configs in t2i.items():
        for elem in configs.keys():
            elem_ids.add(elem)

            if "img2img" in elem:
                print(f'\n[Yapping]: "{elem}" found in preset "{btn}" for txt2img?\n')

    i2i: dict[str, dict] = DATA.get("img2img", {})
    for btn, configs in i2i.items():
        for elem in configs.keys():
            elem_ids.add(elem)

            if "txt2img" in elem:
                print(f'\n[Yapping]: "{elem}" found in preset "{btn}" for img2img?\n')

    return t2i, i2i, elem_ids


def load_triggers() -> tuple[dict, dict, set[str]]:
    btn_ids = set()

    triggers: dict[str, str] = DATA.get("triggers", {})
    t2i: dict[str, str] = {}
    i2i: dict[str, str] = {}

    for btn, moe in triggers.items():

        try:
            mode, event = moe.split("-")
        except ValueError:
            print(f'\n[Yapping]: Invalid mode-event "{moe}" in triggers...!\n')
            continue

        btn_ids.add(btn)

        if mode == "t2i":
            t2i.update({event: btn})
        elif mode == "i2i":
            i2i.update({event: btn})

    return t2i, i2i, btn_ids
