# wrapper.py
import threading
import webpage


def start_flask_server():
    # Disable use_reloader when running Flask in a separate thread
    webpage.run_server(debug=True, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=start_flask_server)
    flask_thread.start()

    # Your main thread can perform other tasks here
    # e.g., start_sound_measurement()
