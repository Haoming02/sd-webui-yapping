from modules import scripts
import gradio as gr

VALID_COMPONENTS: dict[str, gr.components.Component] = {
    "txt2img_width": None,
    "txt2img_height": None,
    "img2img_width": None,
    "img2img_height": None,
    # "selected_scale_tab"
}


class Yapping(scripts.Script):

    def title(self):
        return "Yapping"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def after_component(self, component, **kwargs):
        ID: str = kwargs.get("elem_id", None)

        if ID and ID in VALID_COMPONENTS.keys():
            VALID_COMPONENTS.update({ID: component})

    def ui(self, is_img2img):

        with gr.Blocks():
            btn = gr.Button("Max")

            btn.click(
                fn=lambda: [2048, 2048],
                inputs=None,
                outputs=[
                    VALID_COMPONENTS.get("txt2img_width"),
                    VALID_COMPONENTS.get("txt2img_height"),
                ],
            )

        return None
