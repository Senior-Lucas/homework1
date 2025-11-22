from datetime import datetime as dt

def checktime(func):
    def wrapper():
        time_now = dt.now()
        print(
            f"функция была вызвана в "
            f"{time_now.hour:02d}:{time_now.minute:02d}:{time_now.second:02d} "
            f"{time_now.day:02d}/{time_now.month:02d}/{time_now.year}"
        )
        func()
        print(func.__name__)
    return wrapper


@checktime
def hello_world():
    print("hello world")


hello_world()
