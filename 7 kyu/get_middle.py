def get_middle(string):
    return string[len(string) // 2] if len(string) % 2 != 0 else string[len(string) // 2 - 1: len(string) // 2 + 1]
