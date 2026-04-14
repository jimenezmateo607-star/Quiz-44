import random
from datetime import datetime

def generar_nombre(Heroes=["Himmel", "Heiter", "Eisen", "Frieren"]):
  return random.choice(Heroes)

def generar_clase(Clase=["Heroe","Clérigo","Guerrero","Mago"]):
  return random.choice(Clase)

def generar_hp (A=80, B=120):
  return random.randint(A, B)

def mostrar_fecha (Fecha=datetime.now()):
  return f"Fecha: {Fecha.day}/{Fecha.month}/{Fecha.year}"

print("=== GENERADOR DE AVENTURAS ===")
print(mostrar_fecha())

print("\n=== Heroes Generados ===")
print(f"Heroe 1: {generar_nombre()} | Clase: {generar_clase()} | HP: {generar_hp()}")
print(f"Heroe 2: {generar_nombre()} | Clase: {generar_clase()} | HP: {generar_hp()}")
print(f"Heroe 3: {generar_nombre()} | Clase: {generar_clase()} | HP: {generar_hp()}")
