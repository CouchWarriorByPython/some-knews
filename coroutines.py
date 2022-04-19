def get_generator(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper


@get_generator
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done!')
        else:
            count += 1
            sum += x
            average = round(sum / count, 2)
