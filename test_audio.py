from openai import OpenAI
client = OpenAI(api_key= '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')

audio_file= open("C:/Users/marti/Desktop/HACKATHON/Practice_002.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)