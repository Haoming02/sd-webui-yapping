from scripts.yap_json import load_init, load_presets, load_triggers
from scripts.yap_apply import apply_presets

from modules import scripts, script_callbacks
import gradio as gr


VALID_COMPONENTS: dict[str, gr.components.Component] = {}

TXT2IMG_BUTTONS: dict[str, gr.Button] = {}
IMG2IMG_BUTTONS: dict[str, gr.Button] = {}

TXT2IMG_PRESETS: dict[str, dict] = None
IMG2IMG_PRESETS: dict[str, dict] = None

TXT2IMG_TRIGGERS: dict[str, str] = None
IMG2IMG_TRIGGERS: dict[str, str] = None

REQUIRED_ELEMENTS: set[str] = None
REQUIRED_BUTTONS: set[str] = None

HOOKED_COMPONENTS: list[gr.components.Component] = []


class Yapping(scripts.Script):

    def title(self):
        return "Yapping"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    @staticmethod
    def try_apply():
        if len(HOOKED_COMPONENTS) < len(REQUIRED_ELEMENTS) + len(REQUIRED_BUTTONS):
            return
        if len(TXT2IMG_BUTTONS) < len(TXT2IMG_PRESETS):
            return
        if len(IMG2IMG_BUTTONS) < len(IMG2IMG_PRESETS):
            return

        apply_presets(
            valid_components=VALID_COMPONENTS,
            t2i_buttons=TXT2IMG_BUTTONS,
            i2i_buttons=IMG2IMG_BUTTONS,
            t2i_presets=TXT2IMG_PRESETS,
            i2i_presets=IMG2IMG_PRESETS,
            t2i_triggers=TXT2IMG_TRIGGERS,
            i2i_triggers=IMG2IMG_TRIGGERS,
        )

    def after_component(self, component, **kwargs):
        ID: str = kwargs.get("elem_id", None)
        if not ID:
            return

        if ID in REQUIRED_ELEMENTS:
            VALID_COMPONENTS.update({ID: component})
            HOOKED_COMPONENTS.append(ID)
            Yapping.try_apply()

        elif ID in REQUIRED_BUTTONS:
            assert isinstance(component, gr.Button)
            VALID_COMPONENTS.update({ID: component})
            HOOKED_COMPONENTS.append(ID)
            Yapping.try_apply()

    def ui(self, is_img2img):
        presets: dict = IMG2IMG_PRESETS if is_img2img else TXT2IMG_PRESETS
        buttons: dict = IMG2IMG_BUTTONS if is_img2img else TXT2IMG_BUTTONS

        if not presets:
            return None

        with gr.Row(elem_classes=["yapping_row"]):

            for name in presets.keys():
                btn = gr.Button(name, size="sm", elem_classes=["yapping_btn"])
                buttons.update({name: btn})

        Yapping.try_apply()
        return None


def init():
    load_init()

    global TXT2IMG_PRESETS, IMG2IMG_PRESETS, REQUIRED_ELEMENTS
    TXT2IMG_PRESETS, IMG2IMG_PRESETS, REQUIRED_ELEMENTS = load_presets()

    global TXT2IMG_TRIGGERS, IMG2IMG_TRIGGERS, REQUIRED_BUTTONS
    TXT2IMG_TRIGGERS, IMG2IMG_TRIGGERS, REQUIRED_BUTTONS = load_triggers()


script_callbacks.on_before_ui(init)
