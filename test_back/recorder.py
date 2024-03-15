import sounddevice as sd
import wavio as wv
import datetime
import os
import numpy as np

freq = 44100
duration = 5 # en segundos

if not os.path.exists("./recordings"):
    os.makedirs("./recordings")

print('Recording')

while True:
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d %H:%M:%S")

    # Iniciar grabación con los valores dados de duración y frecuencia de muestreo
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    
    # Esperar hasta que la grabación esté completa
    sd.wait()

    # Normalizar los datos de audio
    max_amplitude = np.max(np.abs(recording))
    if max_amplitude > 1.0:
        recording /= max_amplitude

    # Convertir la matriz NumPy a archivo WAV y guardar
    wv.write(f"./recordings/{filename}.wav", recording, freq, sampwidth=2)
