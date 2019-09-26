def read(filepath):
    '''Write a Python program that repeatedly reads lines from standard input
    until an EOFError is raised, and then outputs those lines in reverse order
    (a user can indicate end of input by typing ctrl-D).'''
    f = open(filepath)
    lines = []
    try:
        line = f.readline()
        if line == '': 
            raise EOFError
        lines.append(line[:-1])

    except EOFError:
        for line in reversed(lines):
            print(line)
        return