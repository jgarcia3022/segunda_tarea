import Bd
from modelo import Slang507


def Agregar():

    palabra_entrada = input("Palabra: ")
    definicion_entrada = input("Definicion: ")
    valor = Slang507(palabra_entrada, definicion_entrada)
    Bd.session.add(valor)
    Bd.session.commit()
    print("Agregado correctamente")

def ImprimeT():
    imprimir1 = Bd.session.query(Slang507).all()
    print(imprimir1)

def Significado():
    palabra = input("Palabra: ")
    significado = Bd.session.query(Slang507).filter_by(palabra=palabra).first()
    print(significado)

def Editar():
    palabra = input("Palabra: ")
    definicion = input(("Definicion: "))
    query = Bd.update(Slang507).values(definicion = definicion)
    query = query.where(Slang507.palabra == palabra)
    Bd.session.execute(query)
    Bd.session.commit()
    print("Editado")

def Eliminar():
    palabra = input("Palabra: ")
    query = Bd.delete(Slang507)
    query = query.where(Slang507.palabra == palabra)
    Bd.session.execute(query)
    Bd.session.commit()
    print("Eliminado")

print("DICCIONARIO DE SLANG Sqlalchemy")
print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:")
print("1: Agregar")
print("2: Editar")
print("3: Eliminar")
print("4: Ver listado")
print("5: Buscar significado")
seleccion = int(input(""))

if seleccion == 1:
    Bd.Base.metadata.create_all(Bd.engine)
    Agregar()

elif seleccion == 2:
    Editar()

elif seleccion == 3:
    Eliminar()

elif seleccion == 4:
    ImprimeT()

elif seleccion == 5:
    Significado()

