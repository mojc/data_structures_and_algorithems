def _choice(data):
    import random
    return data[random.randrange(0, len(data))]

if __name__ == "__main__":
    print(_choice([1,4,6,22,5,6,7]))
    print(_choice('aslkfsalfal'))