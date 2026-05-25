# 1

def verificar_ganador_ronda(jugador, maquina)->str:
    if (jugador == 1 and maquina == 1) or (jugador == 2 and maquina == 2) or (jugador == 3 and maquina == 3):
        return "empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "jugador"
    else:
        return "maquina"
    
# 2

def verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda_actual)->bool:
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    else:
        return True

# 3

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina)->str:
    if aciertos_jugador > aciertos_maquina:
        return "jugador"
    else:
        return "maquina"

# 4

def mostrar_elemento(eleccion)->str:
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    else:
        return "Tijera"






