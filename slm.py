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

# Example usage
if __name__ == "__main__":
    print("Starting continuous sound level measurement...")
    try:
        # Write the header to the CSV if it's the first run
        save_to_csv(["Timestamp", "Sound Level (dB)"])
        
        while True:
            # Measure sound level
            level = sound_level()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Time: {timestamp}, Sound Level: {level} dB")
            
            # Save the data to CSV
            save_to_csv([timestamp, level])
            
            # Wait for 10 seconds before the next measurement
            time.sleep(2)
    except KeyboardInterrupt:
        print("Measurement stopped by user.")
