def write_to_list(seq, index, value):
    try:
        seq[index]=value
    except IndexError as err:
        print('Don’t try buffer overflow attacks in Python!')
    return seq
print(write_to_list([1,2,3,4], 2, 9))
print(write_to_list([1,2,3,4], 5, 9))