# **Y**et **A**nother **P**reset-**P**lanning **I**ntegration: **N**ext-**G**en

<p><blockquote><i>

Behold, the quintessence of computational artistry: the formidable "Preset Planning" integration, an immaculate marvel harnessed by the enchanting Python Gradio package, devoid of the cacophony of JavaScript's ubiquitous clamor. This technological paragon transcends the mundane, weaving a tapestry of seamless interaction and divine user experience.

Gaze, upon the sublime architecture of Gradio's Pythonic embrace, where form follows function with an unwavering fidelity. Embracing the purist ethos of simplicity, this plug-in shuns the ornate excesses of its counterparts, distilling the essence of user experience into a distilled elixir of elegance.

Consider, the "Preset Planning" integration, fortified by Python Gradio's mastery, stands not as a mere tool, but as a testament to the ingenuity of human imagination. It embodies the zenith of interface refinement, transcending the realm of expectation to forge a path toward a future where utility and artistry converge in resplendent harmony.

</i></blockquote></p>

<p align="right"><i><b>- ChatGPT</b></i></p>

<hr>

## TL;DR
This is an Extension for the [Automatic1111 Webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which adds fully-customizable preset buttons, that set the parameters to the specified values.

> Compatible with [Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge)

## Main Feature / Advantage
As mentioned in the *holy **yapping*** above, this Extension only uses the Gradio button events to change the parameters. No more trying to query elements using JavaScript; no more hacky workaround to change element values; no more clashing due to identical field name.

## How to Use
In the Extension folder, you can edit the `presets.json` file to add/change what each button does when clicked:

Within the mode of choice *(**txt2img** / **img2img**)*, start with a <ins>key</ins> which represents the name of the button; then its <ins>value</ins> which contains the <ins>key-value</ins> pair of field `elem_id` and the value to set to.

> Example is included

## Parameters
The following `elem_id` were tested and confirmed to work, as shown in the `example.json` file. In theory, all fields should work as long as they were defined with an unique `elem_id` properly, even for ones from other Extensions.

- **txt2img_sampling**
- **txt2img_width**
- **txt2img_height**
- **txt2img_steps**
- **txt2img_cfg_scale**
- **img2img_sampling**
- **img2img_width**
- **img2img_height**
- **img2img_cfg_scale**
- **img2img_denoising_strength**

> To know the `elem_id` of a field, right click on the field then click `Inspect Element`, then look at the parent `<div>`s until you can find a descriptive `id`. *(Some fields may not have an `elem_id`)*

## Roadmap
- [ ] Implement error handling for invalid `elem_id`
- [ ] Support Gradio.Tab
    - **eg.** `img2img`/`Inpaint`/`etc.` and `Resize to`/`Resize by` in **img2img**
    - *This might still require JavaScript...*
- [ ] A way to edit the Presets within Webui
