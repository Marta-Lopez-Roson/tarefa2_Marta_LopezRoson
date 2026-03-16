from faker import Faker
import random

fake = Faker()
# Dicionario para guardar los usuarios
usuarios = {}

# Crear 15 usuarios
for codigo in range(1, 16):
    usuarios[codigo] = {
        "nome": fake.name(),
        "direccion": fake.address(),
        "email": fake.email(),
        "telefono": fake.phone_number()
    }

# Mostrar todos los usuarios
print("LISTA DE USUARIOS:")

for codigo, datos in usuarios.items():
    print(f"Código: {codigo}")
    print(f"Nome: {datos['nome']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Email: {datos['email']}")
    print(f"Teléfono: {datos['telefono']}")
    print("-" * 40)

# Escoller un usuario aleatorio
codigo_gañador = random.choice(list(usuarios.keys()))
nome_gañador = usuarios[codigo_gañador]["nome"]

print(f"O usuario chamado {nome_gañador} foi o afortunado!")
