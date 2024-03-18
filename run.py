import threading
import sound_level_measurement

def run_sound_level_measurement():
    sound_level_measurement.main()

if __name__ == "__main__":
    measurement_thread = threading.Thread(target=run_sound_level_measurement)
    
    # Starting the thread
    measurement_thread.start()

    # Here, you can add other operations to run in the main thread
    # or start more threads for other tasks

    # Optionally, wait for the measurement thread to finish
    # measurement_thread.join()
