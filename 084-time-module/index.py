import time


def using_while():
    i = 0
    while i < 50:
        i += 1
        print(i)


def using_for():
    for i in range(50):
        print(i)


initial_time = time.time()
using_while()
print(time.time() - initial_time)
using_for()
print(time.time() - initial_time)

time_now = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_now)
print(formatted_time)
