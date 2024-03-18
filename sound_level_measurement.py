import sounddevice as sd
import numpy as np
import csv
import time
from datetime import datetime

def sound_level(duration=1, samplerate=44100):
    """Measure the sound level in dB from the microphone."""
    
    # Record audio for the given duration
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='float64')
    sd.wait()  # Wait until the recording is finished

    # Calculate the RMS of the recording
    rms = np.sqrt(np.mean(recording**2))

    # Convert RMS to dB
    db = 20 * np.log10(rms)

    return db

def save_to_csv(data, filename="sound_levels.csv"):
    """Save the given data to a CSV file."""
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    print("Starting continuous sound level measurement...")
    try:
        save_to_csv(["Timestamp", "Sound Level (dB)"])
        
        while True:
            level = sound_level()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Time: {timestamp}, Sound Level: {level} dB")
            save_to_csv([timestamp, level])
            
            time.sleep(2)  # Adjusted for demonstration
    except KeyboardInterrupt:
        print("Measurement stopped by user.")