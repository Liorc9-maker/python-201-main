def my_enumerate(iterable, start=0):
    result = []
    index = start
    for item in iterable:
        result.append((index, item))
        index += 1
    return result