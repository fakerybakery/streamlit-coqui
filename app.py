"""
Copyright (c) 2022 mrfakename. All rights reserved.
Unauthorized reproduction of this program is strictly prohibited.
HuggingFace: https://huggingface.co/spaces/mrfakename/tts
GitHub: https://github.com/fakerybakery/streamlit-coqui

Version 2.6.1 (December 6, 2022)
"""
import tempfile

import streamlit as st

from neon_tts_plugin_coqui import CoquiTTS


LANGUAGES = list(CoquiTTS.langs.keys())
default_lang = "en"



title = "Neural Text-to-Speech Online"
description = "Convert your text to speech free using Coqui TTS!"
info = """
## About

Ever wanted to generate realistic-sounding text to speech quickly? Well now you can with this new online tool! Generate neural text to speech quickly using Coqui TTS!

Created by [mrfakename](https://mrfake.name/).

## License

Feel free to use generated audio freely (in videos, audio messages, etc).

The code is copyrighted. Please view app.py for license details.

## Credits & Disclaimer

This text to speech tool was influenced by [this](https://huggingface.co/spaces/Gradio-Blocks/neon-tts-plugin-coqui) and uses [this](https://github.com/NeonGeckoCom/neon-tts-plugin-coqui) and [this](https://github.com/coqui-ai/TTS. 

DISCLAIMER: mrfakename is in no way affiliated with Coqui TTS, HuggingFace, GitHub, or NeonAI.
"""



coquiTTS = CoquiTTS()


def tts(text: str, language: str):
    print(text, language)
    # return output
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        coquiTTS.get_tts(text, fp, speaker = {"language" : language})
        return fp.name

st.title(title)
st.subheader(description)
st.markdown(info)
lang = st.selectbox('Please select a language:', (LANGUAGES))
txt = st.text_area("Text")
if st.button('Submit'):
    with st.spinner('Please wait...'):
        audio_file = open(tts(txt, lang), 'rb')
        audio_bytes = audio_file.read()
        st.balloons()
        st.success("Yay! Check out your TTS! P.S. Why not follow my GitHub, I'm @fakerybakery on GitHub!")
        st.audio(audio_bytes, format='audio/wav')
