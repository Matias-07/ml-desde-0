import numpy as np
import matplotlib.pyplot as plt 

N_PUNTOS = 100
DESVIO_RUIDO = 1.5
SEMILLA = 42
W = 3
B = 2


def predecir(valores_x, w, b):
    return w * valores_x + b 

def perdida(valor_real, valor_esperado):
    #error cuadratico medio
    return np.average((valor_esperado - valor_real)**2)

if __name__ == "__main__":
    #creamos el array inicial de valores para X
    array_x = np.linspace(0, 10, N_PUNTOS)

    #creamos el ruido
    generador = np.random.default_rng(SEMILLA)
    array_ruido = generador.normal(0,DESVIO_RUIDO,N_PUNTOS)

    valores_reales_y = 3*array_x + 2

    valores_devio_y = valores_reales_y + array_ruido

    resultados = predecir(array_x, W,B)

    print(perdida(resultados, valores_devio_y))

    #plot - muestra los datos
    fig, ax = plt.subplots(figsize=(20, 6))

    ax.plot(array_x, valores_reales_y, 'o') 
    ax.plot(array_x, valores_devio_y, 'x')

    plt.show() 
    
