def make_readable(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return (f"{hour:02}:{min:02}:{sec:02}")