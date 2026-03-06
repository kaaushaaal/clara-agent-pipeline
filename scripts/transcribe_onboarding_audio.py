import whisper

model = whisper.load_model("tiny")

audio_path = "dataset/bens-electric/audio1975518882.m4a"

result = model.transcribe(audio_path)

output_path = "dataset/bens-electric/onboarding_transcript.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Onboarding transcript created:", output_path)