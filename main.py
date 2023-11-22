from pygame import mixer
import time

def play_sound(sound_file):
    try:
        mixer.init()
        mixer.music.load("eng9_17112023_Final.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
    except Exception:
        pass


def start_playing():
    with open("tries.txt") as f:
        data = f.read()
        is_playing = bool(data)

    with open("tries.txt", mode='w') as f:
        f.write('True')

    if not is_playing:
        sound_file = "eng9_17112023_Final.mp3"
        play_sound(sound_file)


if __name__ == "__main__":
    start_playing()
