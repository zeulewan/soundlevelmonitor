import threading
import sound_level_measurement
import webpage

def start_flask_server():
    # Disable use_reloader when running Flask in a separate thread
    webpage.run_server(debug=True, use_reloader=False)

def run_sound_level_measurement():
    sound_level_measurement.main()

if __name__ == "__main__":
    # Create threads for Flask server and sound level measurement
    flask_thread = threading.Thread(target=start_flask_server)
    measurement_thread = threading.Thread(target=run_sound_level_measurement)

    # Start the threads
    flask_thread.start()
    measurement_thread.start()

    # Here, you can perform other operations in the main thread
    # or handle coordination between the threads if needed

    # Optionally, wait for the threads to finish
    # flask_thread.join()
    # measurement_thread.join()
