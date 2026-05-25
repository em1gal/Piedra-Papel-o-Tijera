from funciones import verificar_ganador_ronda
from funciones import verificar_estado_partida
from funciones import verificar_ganador_partida
from funciones import mostrar_elemento
import random

def jugar_piedra_papel_tijera()->str:

    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda_actual = 1
    
    while verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual):

        jugador = int(input("eliga entre piedra = 1,papel = 2 o tijera = 3: "))
        print("jugador eligio: ",mostrar_elemento(jugador))
        maquina = random.randint(1, 3)
        print("maquina eligio: ",mostrar_elemento(maquina))
        ronda = verificar_ganador_ronda(jugador, maquina)

        print(ronda, " es el ganador de la ronda")

        ronda_actual += 1
        if ronda == "jugador":
            aciertos_jugador += 1
        elif ronda == "maquina":
            aciertos_maquina += 1

    return verificar_ganador_partida(aciertos_jugador, aciertos_maquina)

resultado = jugar_piedra_papel_tijera()

print("el ganador del piedra,papel o tijera es: ", resultado)
