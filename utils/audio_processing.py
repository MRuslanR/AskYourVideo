from moviepy import VideoFileClip
import os

def convert_video_to_audio(video_path, output_dir):
    audio_path = os.path.join(output_dir, "audio.wav")

    video_clip = VideoFileClip(video_path)
    video_clip.audio.write_audiofile(
        audio_path,
        codec="pcm_s16le",
        ffmpeg_params=["-ac", "1", "-ar", "16000"]
    )

    return audio_path