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
  return(f"{nombre}: {hp}/{hp_max}")


def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de daño!")

hp_hero=100
hp_enemigo=50

print("=== Estado Inicial ===")
print(mostrar_estado("Hero", hp_hero))
print(mostrar_estado("Enemigo", hp_enemigo))
daño = calcular_dano(25,10)

realizar_ataque("\nHero","Enemigo", daño)
hp_enemigo = aplicar_dano(hp_enemigo,daño)
print(mostrar_estado("Enemigo",hp_enemigo ))

realizar_ataque("\nHero","Enemigo", daño)
hp_enemigo = aplicar_dano(hp_enemigo,daño)
print(mostrar_estado("Enemigo",hp_enemigo ))
