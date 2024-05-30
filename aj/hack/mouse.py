import win32api
import threading
import time

def block_mouse(duration) -> None:
    """Blocks the mouse by setting the position to 0x0. The duration is in seconds or enter 'infinite' to never stop it."""
    
    def set_pos(duration):
        if duration == "infinite":
            while True:
                win32api.SetCursorPos((0,0))
        else:
            current_time = time.time()
            end_time = current_time + duration

            while time.time() < end_time:
                win32api.SetCursorPos((0,0))
        

    threading.Thread(target=set_pos, args=[duration]).start()