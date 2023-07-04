import func
path = "./audio/Recording.wav"

func.hello()
print("\nFull text:", func.get_large_audio_transcription_silence(path))

print("\nFull text:", func.get_large_audio_transcription_interval(path))