import json

def getData():
	try:
		capacidadJson = open("capacidad.json",'r')
		capacidad = json.load(capacidadJson)
		capacidadJson.close()

		dimensionJson = open("dimension.json",'r')
		dimension = json.load(dimensionJson)
		dimensionJson.close()

		demandasJson = open("demandas.json",'r')
		demandas = json.load(demandasJson)
		demandasJson.close()

		matrixJson = open("matrix.json",'r')
		matrix = json.load(matrixJson)
		matrixJson.close()

		return capacidad, dimension, demandas, matrix

	except:
		print("falta cargar los archivos de entrada")

def createOutput():
	capacidad, dimension, demandas, matrix = getData()

	mapaDemandas =  {index + 1: value for index, value in enumerate(demandas)}

	primerasSucursales = dict(filter(lambda x: x[1] >= 0, mapaDemandas.items()))

	lists = []

	print("Arranca procesamiento")

	for k in primerasSucursales.keys():
		print("Creando iteracion para sucursal {} con demanda {}".format(k,demandas[k-1]))
		secuencia = []
		secuencia.append(k)
		visitados = set()
		visitados.add(k)
		pendientes = set(range(1,dimension + 1)) - visitados
		acum = 0
		acum += demandas[k - 1]
		while (len(pendientes) > 0):
			for i in pendientes:
				if ((i not in secuencia)
					and (acum + demandas[i -1] >= 0)
					and (acum + demandas[i -1] <= capacidad)):
					acum += demandas[i - 1]
					secuencia.append(i)
					visitados.add(i)
			
			pendientes = pendientes - visitados

		lists.append(list(secuencia))

	distancias=[]
	for i in range(len(lists)):
		acum = 0
		for j in range(len(lists) - 1):
			acum += matrix[lists[i][j] - 1][lists[i][j+1] - 1]
		distancias.append(acum)

	minDistancia = min(distancias)
	nroIteracion = distancias.index(minDistancia)
	print("La minima distancia es {} y paso en la iteracion numero {}".format(minDistancia, nroIteracion))

	fileOut = open("output.txt","w")
	for i in range(len(lists[nroIteracion])):
		fileOut.write("{} ".format(lists[nroIteracion][i]))
	fileOut.close()

createOutput()