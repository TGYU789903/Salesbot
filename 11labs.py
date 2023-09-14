from elevenlabs import generate, stream, set_api_key
import datetime

set_api_key("60ec591316cdf20717559a5e9d5ee30e")

now = datetime.datetime.now()
print(f'"Main function began: " {now.strftime("%Y-%m-%d %H:%M:%S")}')

def text_stream():
    yield "Hi there, I'm Eleven "
    yield "I'm a text to speech API "

audio_stream = generate(
    text=text_stream(),
    voice="Vikram",
    stream=True
)

stream(audio_stream)
# Save the audio stream to a file
with open('output_audio.mp3', 'wb') as audio_file:
    for chunk in audio_stream:
        audio_file.write(chunk)

print("Audio saved to 'output_audio.mp3'")
