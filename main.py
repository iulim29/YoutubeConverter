import os.path


def mp42mp3(our_mp4_file):
    base, out = os.path.splitext(our_mp4_file)
    new_file = base + '.mp3'
    os.rename(our_mp4_file, new_file)
    return our_mp4_file


new_file2 = mp42mp3("my_song.mp4")


