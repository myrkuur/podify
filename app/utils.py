from uuid import uuid4

from app import tts_client as client


def tts(text: str) -> str:
    """Converts a given text to realistic speech and returns the saved audio."""
    generator = client.text_to_speech.convert(
        voice_id="nPczCjzI2devNBz1zQrb",
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_multilingual_v2",
    )
    filepath = f"output/{uuid4().hex}.mp3"
    with open(filepath, 'wb') as f:
            for chunk in generator:
                f.write(chunk)
    return filepath