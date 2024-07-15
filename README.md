# **Y**et **A**nother **P**reset-**P**lanning **I**ntegration: **N**ext-**G**en

<p><blockquote><i>

Behold, the quintessence of computational artistry: the formidable "Preset Planning" integration, an immaculate marvel harnessed by the enchanting Python Gradio package, devoid of the cacophony of JavaScript's ubiquitous clamor. This technological paragon transcends the mundane, weaving a tapestry of seamless interaction and divine user experience.

Gaze, upon the sublime architecture of Gradio's Pythonic embrace, where form follows function with an unwavering fidelity. Embracing the purist ethos of simplicity, this plug-in shuns the ornate excesses of its counterparts, distilling the essence of user experience into a distilled elixir of elegance.

Consider, the "Preset Planning" integration, fortified by Python Gradio's mastery, stands not as a mere tool, but as a testament to the ingenuity of human imagination. It embodies the zenith of interface refinement, transcending the realm of expectation to forge a path toward a future where utility and artistry converge in resplendent harmony.

</i></blockquote></p>

<p align="right"><i><b>- ChatGPT</b></i></p>

<hr>

# SD Webui Yapping
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which adds fully-customizable preset buttons, that set specified parameters to specified values when clicked.

> Compatible with [Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)

<p align="center">
<img src="ui.jpg"><br>
Example Buttons<br>
(used with <a href="https://github.com/Haoming02/sd-webui-tabs-extension">Tabs Extension</a>)
</p>

#### Main Advantage over other Implementations
As mentioned in the *holy **yapping*** above, this Extension finds the fields during the UI setup process via Python, and uses the Gradio button events to change the parameters.

No more trying to query elements using JavaScript; no more hacky workaround to change element values; no more clashing due to identical field name.

## How to Use
On a fresh install, the Extension will automatically rename `example.json` to `presets.json`, to avoid overriding users' presets.

- Within the `presets.json` file:
    - There are 2 entries, `txt2img` and `img2img`, representing the mode that the buttons will show up in.

- Inside each mode:
    - You can have multiple entries. Each entry is a preset button, where the <ins>key</ins> is the name of the button.

- Under each button:
    - Add <ins>key-value</ins> pairs of the parameter field `elem_id` and the value to set to.

> Refer to the `presets.json` for included examples and formats

#### Parameters
Listed below are some `elem_id` that were tested and confirmed to work.

In theory, most parameters should work as long as they are Gradio components and were defined with an unique `elem_id` properly, even for ones from Extensions.

> **txt2img:** `txt2img_sampling`, `txt2img_width`, `txt2img_height`, `txt2img_steps`, `txt2img_cfg_scale`

> **img2img:** `img2img_sampling`, `img2img_width`, `img2img_height`, `img2img_steps`, `img2img_cfg_scale`, `img2img_denoising_strength`

To find the `elem_id` of a parameter, right click on the field and click `Inspect Element`, then look through the parent `<div>`s until you can find a descriptive `id`. *(**Note:** Some fields may not have an `elem_id`)*

## Roadmap
- [X] Implement error handling for invalid `elem_id`
- [ ] A way to edit the Presets within Webui

## Pain...
- [ ] Support Gradio.Tab
    - **eg.** `img2img`/`Inpaint`/`etc.` and `Resize to`/`Resize by` in **img2img**
    - This **will** require JavaScript...
- [ ] Add ways to trigger Preset
    - This **will** require JavaScript...
