print("Act 9 clase humano")
print("Santiago Sanchez Mat: 22308851281099")
# Zona de clases

class humano1099:
    # Zona de atributos dentro de la clase
    edad=0
    genero=""
    fecha_nac=""
    estatura=0
    peso=0
    ojos=""
    
    # Zona de funciones dentro de la clase
    def correr1099(self, n):
        print(f"{n} está corriendo")
    def brincar1099(self, n):
        print(f"{n} está brincando")
    def caminar1099(self, n):
        print(f"{n} está caminando")
    def hablar1099(self, n):
        print(f"{n} está hablando")
    def comer1099(self, n):
        print(f"{n} está comiendo")
    
# Zona de creacion de objetos
Santiago=humano1099()
Venti=humano1099()
# Zona de usando objetos
print("Resultados para Santiago")
Santiago.edad=17
Santiago.genero="Masculino"
Santiago.fecha_nac="13 Febrero 2007"
Santiago.peso=52
Santiago.estatura=1.64
Santiago.ojos="Negro"
print(f"Edad: {Santiago.edad}")
print(f"Genero: {Santiago.genero}")
print(f"Fecha de nacimiento: {Santiago.fecha_nac}")
print(f"Peso: {Santiago.peso} kg.")
print(f"Estatura: {Santiago.estatura} m.")
print(f"Color de ojos: {Santiago.ojos}")
print("-------------------")
Santiago.correr1099("Santiago")
Santiago.brincar1099("Santiago")
Santiago.caminar1099("Santiago")
Santiago.hablar1099("Santiago")
Santiago.comer1099("Santiago")
print("-------------------")
print("-------------------------------------")
print("-------------------")
print("Resultados para Venti")
Venti.edad=18
Venti.genero="Femenino_"
Venti.fecha_nac="1 Junio 2006"
Venti.peso=49
Venti.estatura=1.62
print(f"Edad: {Venti.edad}")
print(f"Genero: {Venti.genero}")
print(f"Fecha de nacimiento: {Venti.fecha_nac}")
print(f"Peso: {Venti.peso} kg.")
print(f"Estatura: {Venti.estatura} m.")
print("-------------------")
Venti.correr1099("Venti")
Venti.brincar1099("Venti")
Venti.caminar1099("Venti")
Venti.hablar1099("Venti")