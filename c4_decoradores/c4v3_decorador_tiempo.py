import time


def medir_tiempo_ejecucion(funcion):

    def wrapper():
        inicio = time.time()
        print("Ejecutando la función decorada...")
        print("Hora de inicio:", inicio)
        
        funcion()
        fin = time.time()
        tiempo_total = fin - inicio
        print("Hora de finalización:", fin)
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


@medir_tiempo_ejecucion
def recorrer_ciclo():

    for i in range(5):
        print(i)
        #time.sleep(1)


recorrer_ciclo()
