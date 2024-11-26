from datetime import datetime
import statistics

class Experimento:
    def __init__(self, nombre, fechaRealizacion, tipo, resultados):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipo = tipo
        self.resultados = resultados

# Función para agregar un experimento
def agregarExperimento(listaExperimentos):
    nombre = input("Ingrese el nombre del experimento: ")
    fechaRealizacion_str = input("Ingrese la fecha de realización (DD/MM/YYYY): ")
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida. Por favor ingrese en el formato DD/MM/YYYY.")
        return
    
    tipo = input("Ingrese el tipo de experimento (Química, Biología, Física): ")
    resultados_str = input("Ingrese los resultados obtenidos, separados por comas: ")
    try:
        resultados = list(map(float, resultados_str.split(",")))
    except ValueError:
        print("Resultados no válidos. Use números separados por comas.")
        return
    
    experimento = Experimento(nombre, fechaRealizacion, tipo, resultados)
    listaExperimentos.append(experimento)
    print("¡Experimento agregado exitosamente!")

# Función para visualizar los experimentos
def visualizarExperimentos(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos para visualizar.")
        return
    
    for i, experimento in enumerate(listaExperimentos, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {experimento.nombre}")
        print(f"Fecha de Realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Tipo: {experimento.tipo}")
        print(f"Resultados: {experimento.resultados}")

# Función para analizar los resultados de los experimentos
def analizarResultados(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos para analizar.")
        return
    
    for experimento in listaExperimentos:
        promedio = statistics.mean(experimento.resultados)
        maximo = max(experimento.resultados)
        minimo = min(experimento.resultados)
        print(f"\nExperimento: {experimento.nombre}")
        print(f"Promedio de resultados: {promedio:.2f}")
        print(f"Máximo resultado: {maximo:.2f}")
        print(f"Mínimo resultado: {minimo:.2f}")

# Función para comparar experimentos
def compararExperimentos(listaExperimentos):
    if len(listaExperimentos) < 2:
        print("Debe haber al menos dos experimentos para comparar.")
        return
    
    print("\nComparación de experimentos:")
    for i, experimento in enumerate(listaExperimentos, start=1):
        promedio = statistics.mean(experimento.resultados)
        print(f"{i}. {experimento.nombre} - Promedio: {promedio:.2f}")
    
    mejor_experimento = max(listaExperimentos, key=lambda e: statistics.mean(e.resultados))
    peor_experimento = min(listaExperimentos, key=lambda e: statistics.mean(e.resultados))
    
    print(f"\nMejor experimento: {mejor_experimento.nombre} - Promedio: {statistics.mean(mejor_experimento.resultados):.2f}")
    print(f"Peor experimento: {peor_experimento.nombre} - Promedio: {statistics.mean(peor_experimento.resultados):.2f}")

# Función para generar un informe
def generarInforme(listaExperimentos):
    if not listaExperimentos:
        print("No hay experimentos para generar un informe.")
        return
    
    with open("informe_experimentos.txt", "w") as archivo:
        for experimento in listaExperimentos:
            archivo.write(f"Nombre: {experimento.nombre}\n")
            archivo.write(f"Fecha de Realización: {experimento.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Tipo: {experimento.tipo}\n")
            archivo.write(f"Resultados: {experimento.resultados}\n")
            archivo.write("\n")
    print("¡Informe generado exitosamente!")

# Menú principal
def menu():
    listaExperimentos = []
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar experimento")
        print("2. Visualizar experimentos")
        print("3. Analizar resultados")
        print("4. Comparar experimentos")
        print("5. Generar informe")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregarExperimento(listaExperimentos)
        elif opcion == "2":
            visualizarExperimentos(listaExperimentos)
        elif opcion == "3":
            analizarResultados(listaExperimentos)
        elif opcion == "4":
            compararExperimentos(listaExperimentos)
        elif opcion == "5":
            generarInforme(listaExperimentos)
        elif opcion == "6":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
    
