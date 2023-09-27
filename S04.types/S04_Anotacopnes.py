from typing import Annotated

def say_hi(name: Annotated[str, 'Ests es un conjunto de datos']) -> str:
    return f"Hello {name}"