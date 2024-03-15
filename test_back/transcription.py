import sys
sys.path.append('c:/users/marti/appdata/local/packages/pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0/localcache/local-packages/python310/site-packages')
# import config
import whisper
import os, glob


TRANSCRIPT_FILE = './transcribedText.txt'

# find most recent files in a directory
recordings_dir = os.path.join('recordings', '*')

model = whisper.load_model("base")

# list to store which wav files have been transcribed
transcribed = []

while True:
    # get most recent wav recording in the recordings directory
    files = sorted(glob.iglob(recordings_dir), key=os.path.getctime, reverse=True)
    if len(files) < 1:
        continue
    
    latest_recording = files[0]
    latest_recording_filename = latest_recording.split('/')[1]

    if os.path.exists(latest_recording) and not latest_recording in transcribed:
        audio = whisper.load_audio(latest_recording)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        options = whisper.DecodingOptions(language= 'sp', fp16=False)

        result = whisper.decode(model, mel, options)

        if result.no_speech_prob < 0.5:
            print(result.text)

            # append text to transcript file
            with open(TRANSCRIPT_FILE, 'a') as f:
                f.write(result.text)
        
            # save list of transcribed recordings so that we don't transcribe the same one again
            transcribed.append(latest_recording)