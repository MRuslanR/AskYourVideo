import torch
from transformers import pipeline


def transcribe_audio(audio_path):
    device = "cpu"
    if torch.cuda.is_available():
        device = "cuda"
    if torch.mps.is_available():
        device = "mps"

    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-small",
        device=device,
        chunk_length_s=30,
    )

    return pipe(
        audio_path,
        batch_size=8,
        return_timestamps=True
    )