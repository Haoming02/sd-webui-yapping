from modules import scripts, script_callbacks
from scripts.yap_json import load_presets
import gradio as gr


TXT2IMG_PRESETS: dict[str, dict] = None
IMG2IMG_PRESETS: dict[str, dict] = None
REQUIRED_COMPONENTS: list[str] = None
VALID_COMPONENTS: dict[str, gr.components.Component] = {}


def init():
    global TXT2IMG_PRESETS, IMG2IMG_PRESETS, REQUIRED_COMPONENTS
    TXT2IMG_PRESETS, IMG2IMG_PRESETS, REQUIRED_COMPONENTS = load_presets()


class Yapping(scripts.Script):

    def title(self):
        return "Yapping"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def after_component(self, component, **kwargs):
        ID: str = kwargs.get("elem_id", None)

        if ID in REQUIRED_COMPONENTS:
            VALID_COMPONENTS.update({ID: component})

    @staticmethod
    def validate_components(presets: dict):
        for name, preset in presets.items():
            keys = list(preset.keys())
            for elem in keys:
                if elem not in VALID_COMPONENTS.keys():
                    print(
                        f'\n[Yapping] Component with elem_id "{elem}" in preset "{name}" not found...\n'
                    )
                    del preset[elem]

    def ui(self, is_img2img):
        PRESETS = IMG2IMG_PRESETS if is_img2img else TXT2IMG_PRESETS
        Yapping.validate_components(PRESETS)

        def apply_presets(preset: str):
            target_values: list[object] = PRESETS[preset].values()
            return list(target_values)

        with gr.Row(elem_classes=["yapping_row"]):

            for preset_name, preset_contents in PRESETS.items():

                target_components: list[str] = [
                    VALID_COMPONENTS[elem_id] for elem_id in preset_contents.keys()
                ]

                btn = gr.Button(preset_name, size="sm", elem_classes=["yapping_btn"])
                btn.click(
                    fn=apply_presets,
                    inputs=[btn],
                    outputs=target_components,
                    show_progress="hidden",
                )

        return None


script_callbacks.on_before_ui(init)
