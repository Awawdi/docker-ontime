import fire

class Calculator():
    def add(x, y):
        return x + y

if __name__ == '__main__':
    fire.Fire(Calculator)