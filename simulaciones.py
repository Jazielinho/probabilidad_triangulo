
import tqdm
import random
import matplotlib.pyplot as plt
from typing import Tuple


def romper_palillo(longitud: float) -> Tuple[float, float, float]:
    '''
    divide un palillo en 3 partes
    '''
    x = random.uniform(a=0, b=longitud)
    y = random.uniform(a=0, b=longitud)
    
    a = min(x, y)
    b = abs(x - y)
    c = longitud - (a + b)
    
    return a, b, c


def es_triangulo(a: float, b: float, c: float) -> bool:
    '''
    Determina si los lados de un triángulo son válidos.
    '''
    return a + b > c and a + c > b and b + c > a


def simula_probabilidad(longitud: float = 1.0, num_iter: int = 1000) -> float:
    '''
    Simula la probabilidad de que un palillo se rompa en 3 partes.
    '''
    num_triangulos_formados = 0
    for _ in range(num_iter):
        a, b, c = romper_palillo(longitud)
        if es_triangulo(a, b, c):
            num_triangulos_formados += 1
    return num_triangulos_formados / num_iter


if __name__ == '__main__':
    iteraciones = range(1, 10000)
    probabilidades = [simula_probabilidad(num_iter=i) for i in tqdm.tqdm(iteraciones)]

    plt.plot(iteraciones, probabilidades)
    plt.axhline(y=0.25, color='r', linestyle='-')