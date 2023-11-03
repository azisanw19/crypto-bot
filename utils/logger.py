import datetime

class Log():
    def d(tag: str, message: str):
        print(f'{datetime.datetime.now()}\td [{tag}] {message}')