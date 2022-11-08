import tempfile

import streamlit as st

from neon_tts_plugin_coqui import CoquiTTS


LANGUAGES = list(CoquiTTS.langs.keys())
default_lang = "en"



title = "🐸💬 - NeonAI Coqui AI TTS Plugin"
description = "🐸💬 - a deep learning toolkit for Text-to-Speech, battle-tested in research and production"
info = "more info at [Neon Coqui TTS Plugin](https://github.com/NeonGeckoCom/neon-tts-plugin-coqui), [Coqui TTS](https://github.com/coqui-ai/TTS)"



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
txt = st.text_area("Text")
if st.button('Submit'):
    audio_file = open(tts(txt, "en"), 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav')
