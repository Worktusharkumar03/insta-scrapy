# Transcriber Module
# Uses Whisper (open-source) for speech-to-text

import whisper

def transcribe_audio(audio_path, model_size='base'):
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_path)
    return result['text']

# Example usage:
# text = transcribe_audio('downloads/video.mp4')
# print(text)
