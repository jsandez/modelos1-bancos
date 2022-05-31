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

def minimoConDemandasValidas(demandas, dimension, matrix, minX, capacidad):
	demandasMinX = {index + 1: demandas[minX - 1] + demandas[index] for index, value in enumerate(range(dimension))}
	demandasMinXFiltradas = dict(filter(lambda x: x[1] >= 0 and x[1] <= capacidad and x[0] != minX, demandasMinX.items()))
	distanciasDemandasFiltradas = {index: matrix[minX -1][index - 1] for index, value in demandasMinXFiltradas.items()}
	return min(distanciasDemandasFiltradas.items(), key = lambda x: x[1])

def getSucursalesIniciales(demandas, dimension, capacidad, matrix, sucDemPositiva):
	minX = list(sucDemPositiva)[0]
	minimoPar = minimoConDemandasValidas(demandas, dimension, matrix, minX, capacidad)
	minimo = minimoPar[1]
	minY = minimoPar[0]

	for i in sucDemPositiva:
		minimoPar = minimoConDemandasValidas(demandas, dimension, matrix, i, capacidad)
		
		if (minimoPar[1] < minimo):
			minimo = minimoPar[1]
			minX = i
			minY = minimoPar[0]
	
	return minimo, minX, minY


def createOutput():
	capacidad, dimension, demandas, matrix = getData()

	mapaDemandas =  {index + 1: value for index, value in enumerate(demandas)}

	sucDemPositiva = dict(filter(lambda x: x[1] >= 0, mapaDemandas.items()))

	secuencia = []

	print("Buscando dos primeras sucursales")
	minimo, minX, minY = getSucursalesIniciales(demandas, dimension, capacidad, matrix, sucDemPositiva.keys())

	print("La minima distancia es {} y pasa en X: {} e Y: {}".format(minimo, minX, minY))
	secuencia.append(minX)
	secuencia.append(minY)
	noVisitados = set(range(1,dimension + 1))
	noVisitados.remove(minX)
	noVisitados.remove(minY)

	print("Arranca procesamiento")

	while (len(secuencia) < dimension):
		print("Iteracion: {}".format(len(secuencia)))

		acum = 0
		for i in secuencia:
		 	acum += demandas[i-1]

		demandasTemp = {value: acum + demandas[value - 1] for value in noVisitados}
		demandasTempFiltradas = dict(filter(lambda x: x[1] >= 0 and x[1] <= capacidad and x[0] in noVisitados, demandasTemp.items()))
		distanciasDemandasFiltradas = {index: matrix[secuencia[-1] - 1][index - 1] for index, value in demandasTempFiltradas.items()}
		minimoPar = min(distanciasDemandasFiltradas.items(), key = lambda x: x[1])
		noVisitados.remove(minimoPar[0])
		secuencia.append(minimoPar[0])

	minDistancia = 0
	for i in range(len(secuencia) - 1):
		minDistancia += matrix[secuencia[i] - 1][secuencia[i+1] - 1]

	print("La minima distancia es {}".format(minDistancia))

	fileOut = open("output.txt","w")
	for i in range(len(secuencia)):
		fileOut.write("{} ".format(secuencia[i]))
	fileOut.close()

createOutput()