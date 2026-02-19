import gradio as gr

try:
    from gradio.layouts.tabs import Tabs
except ImportError:
    from gradio.layouts import Tabs

HOOKED: bool = False


def validate_presets(valid_components: dict, presets: dict):
    for name, configs in presets.items():
        components = list(configs.keys())

        for elem_id in components:
            if elem_id not in valid_components:
                print(f'\n[Yapping] elem_id "{elem_id}" for "{name}" not found...\n')
                del configs[elem_id]


def validate_triggers(valid_components: dict, presets: dict, triggers: dict):
    events = list(triggers.keys())

    for event in events:
        if event not in presets:
            print(f'\n[Yapping] Event "{event}" not found...\n')
            del triggers[event]
            continue

        btn = triggers[event]
        if btn not in valid_components:
            print(f'\n[Yapping] Button with elem_id "{btn}" not found...\n')
            del triggers[event]


def apply_presets(
    valid_components: dict,
    t2i_buttons: dict,
    i2i_buttons: dict,
    t2i_presets: dict,
    i2i_presets: dict,
    t2i_triggers: dict,
    i2i_triggers: dict,
):
    global HOOKED
    if HOOKED:
        return

    validate_presets(valid_components, t2i_presets)
    validate_presets(valid_components, i2i_presets)
    validate_triggers(valid_components, t2i_presets, t2i_triggers)
    validate_triggers(valid_components, i2i_presets, i2i_triggers)

    TABS: dict[str, int] = {}

    def apply_presets_t2i(preset: str):
        target_values = list(t2i_presets[preset].values())
        if (idx := TABS.get(preset, None)) is not None:
            target_values[idx] = gr.update(selected=target_values[idx])

        if len(target_values) == 1:
            return target_values[0]
        else:
            return target_values

    for name, configs in t2i_presets.items():
        button = t2i_buttons[name]

        target_components: list[str] = [
            valid_components[elem_id] for elem_id in configs.keys()
        ]

        for i, comp in enumerate(target_components):
            if isinstance(comp, Tabs):
                TABS[name] = i

        button.click(
            fn=apply_presets_t2i,
            inputs=button,
            outputs=target_components,
            show_progress="hidden",
        )

        if name in t2i_triggers.keys():
            valid_components[t2i_triggers[name]].click(
                fn=apply_presets_t2i,
                inputs=button,
                outputs=target_components,
                show_progress="hidden",
            )

    def apply_presets_i2i(preset: str):
        target_values = list(i2i_presets[preset].values())
        if (idx := TABS.get(preset, None)) is not None:
            target_values[idx] = gr.update(selected=target_values[idx])

        if len(target_values) == 1:
            return target_values[0]
        else:
            return target_values

    for name, configs in i2i_presets.items():
        button = i2i_buttons[name]

        target_components: list[str] = [
            valid_components[elem_id] for elem_id in configs.keys()
        ]

        for i, comp in enumerate(target_components):
            if isinstance(comp, Tabs):
                TABS[name] = i

        button.click(
            fn=apply_presets_i2i,
            inputs=button,
            outputs=target_components,
            show_progress="hidden",
        )

        if name in i2i_triggers.keys():
            valid_components[i2i_triggers[name]].click(
                fn=apply_presets_i2i,
                inputs=button,
                outputs=target_components,
                show_progress="hidden",
            )

    if (preset_count := len(t2i_presets) + len(i2i_presets)) > 0:
        print(f"[Yapping] Hooked {preset_count} Presets")
    if (trigger_count := len(t2i_triggers) + len(i2i_triggers)) > 0:
        print(f"[Yapping] Hooked {trigger_count} Triggers")

    HOOKED = True


def reset():
    global HOOKED
    HOOKED = False
