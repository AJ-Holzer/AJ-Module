import pygame, time

def play_music(file: str) -> None:
    """
    Plays a music file.
    
    :param file: The music file path.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
