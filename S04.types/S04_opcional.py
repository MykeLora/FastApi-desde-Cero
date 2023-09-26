from typing import Opcional

def say_hi(name: Opcional[str] = None):
    if name is not None:
        print(f"Hey {name}!")

    else:
        print("Hello world")    