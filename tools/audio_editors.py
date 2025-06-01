from langchain_community.tools import ElevenLabsText2SpeechTool


def tts():
    tts = ElevenLabsText2SpeechTool()
    return tts
