def calcular_dano(ataque, defensa):
    result = ataque - defensa
    if result >= 0: 
        return (result)
    else:
        return(0)
def aplicar_dano(hp_actual, dano):
    result = hp_actual-dano
    if result <= 0:
        return(0)
    else:
        return(result)
    
def mostrar_estado(nombre, hp, hp_max=100):
    print(f"El heroe {nombre} tiene {hp/hp_max}")
    return(hp/hp_max)

def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de dano!)

hp_hero=100
hp_enemigo=50
