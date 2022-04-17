from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('dima')
g2 = gen2(5)


tasks = [g1, g2]


def mac(s):
    return f'{s* 2} -- int' if isinstance(s, int) else s + ' -- str'


while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(mac(i))
        tasks.append(task)
    except StopIteration:
        pass