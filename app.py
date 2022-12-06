"""
Copyright (c) 2022 mrfakename. All rights reserved.
Unauthorized reproduction of this program is strictly prohibited.
HuggingFace: https://huggingface.co/spaces/mrfakename/tts
GitHub: https://github.com/fakerybakery/streamlit-coqui
"""
import tempfile

import streamlit as st

from neon_tts_plugin_coqui import CoquiTTS


LANGUAGES = list(CoquiTTS.langs.keys())
default_lang = "en"



title = "🐸💬 - NeonAI Coqui AI TTS Plugin"
description = "🐸💬 - a deep learning toolkit for Text-to-Speech, battle-tested in research and production"
info = "more info at [Neon Coqui TTS Plugin](https://github.com/NeonGeckoCom/neon-tts-plugin-coqui), [Coqui TTS](https://github.com/coqui-ai/TTS) - this is a streamlit version of [this](https://huggingface.co/spaces/Gradio-Blocks/neon-tts-plugin-coqui)"



coquiTTS = CoquiTTS()


def tts(text: str, language: str):
    print(text, language)
    # return output
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        coquiTTS.get_tts(text, fp, speaker = {"language" : lang})
        return fp.name

st.title(title)
st.subheader(description)
st.markdown(info)
lang = st.selectbox('Please select a language:', (LANGUAGES))
txt = st.text_area("Text")
if st.button('Submit'):
    with st.spinner('Wait for it...'):
        audio_file = open(tts(txt, "en"), 'rb')
        audio_bytes = audio_file.read()
        st.balloons()
        st.success("Yay! Check out your TTS! P.S. Why not follow my GitHub, I'm @fakerybakery on GitHub!")
        st.audio(audio_bytes, format='audio/wav')
