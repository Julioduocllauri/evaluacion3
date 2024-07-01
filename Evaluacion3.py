import os

os.system('cls')



titulo = f'''{"Listado de vehiculos"}

{"-" *105}

{"Marca" :<15}{"Año ":<15}{"kilometraje":<15}{"Cost.reparacion":>20}{"Impuesto":>15}{"Costo total ":>15}

{"-" *105}

'''

menu = f'''

1. Registrar marca

2. Listar todos los vehiculos

3. Imprimir 

4. Salir del programa

'''

marcas = ['toyota','ford','chevrolet']

listamarca = []



def registrar():

    while True:

        try:

            marca = input(f"Marca: {marcas}: ").strip().lower()

            año = input(f"Año: : ").strip()

            kilometraje = int(input("Ingrese el kilometraje: "))
            costoestimado = int(input("Ingrese costo estimado: "))

            if len(marca)> 0 and marca in marcas and kilometraje > 0 and costoestimado > 0:

                impuesto = round(costoestimado * 0.08)
                total = round(costoestimado + impuesto)
                

                listamarca.append([marca,año,kilometraje,costoestimado,impuesto,total])

                input("Marca agregado con exito...")

                break

        except:

            input("Ingreso algo mal, intentelo de nuevo...")



def listar():

    lista = titulo

    for i in listamarca:

        lista += f"{i[0]:<15}"

        lista += f"{i[1]:<15}"

        lista += f"{i[2]:<15}"

        lista += f"{i[3]:>20}"

        lista += f"{i[4]:>15}"

        lista += f"{i[5]:>15}"

        lista += "\n"

    return lista



def listarxmarca(marca):

    lista = titulo

    for i in listamarca:

        if i[0] == marca:

            lista += f"{i[0]:<15}"

            lista += f"{i[1]:<15}"

            lista += f"{i[2]:<15}"

            lista += f"{i[3]:>20}"

            lista += f"{i[4]:>15}"

            lista += f"{i[5]:>15}"

            lista += "\n"

    return lista



def imprimir():

        marca = input(f"cargo a imprimir ['Todos' / {marcas}]: ".strip().lower())

        if marca == 'todos':

            with open("todos.txt","w") as archivo:

                archivo.write(listar())

        elif marca in marcas:

            with open(marca+".txt","w") as archivo:

                archivo.write(listarxmarca(marca))
        else: 

            print("ALGO MAL ESCRITO ")



while True:

    try:

        opc = input(menu)

        if opc == '4':

            break

        elif opc == '1':

            registrar()

        elif opc == '2':

            marca = input(f"marca a mostrar ['Todos' / {marcas}]: ".strip().lower())

            if marca == 'todos':

                print(listar())

            elif marca in marcas:

                print(listarxmarca(marca))

        elif opc == '3':

            imprimir()





    except Exception as e:

        input(f"excepc menu : {str(e)}")