import win32api #type:ignore
import threading
import time

def block_mouse(duration: int) -> None:
    """
    Blocks the mouse in a new thread by setting the position to 0x0.\n
    The duration is in seconds or enter 'infinite' to never stop it.\n
    While the thread is running, you are not able to press ctrl+alt+delete!

    :param duration: How long the mouse should be moved.
    """
    
    def set_pos(duration: int) -> None:
        if duration == -1:
            while True:
                win32api.SetCursorPos((0,0))
        else:
            current_time = time.time()
            end_time = current_time + duration

            while time.time() < end_time:
                win32api.SetCursorPos((0,0))
        

    threading.Thread(target=set_pos, args=[duration]).start()
