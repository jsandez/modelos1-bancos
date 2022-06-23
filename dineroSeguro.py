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

def minimoConDemandasValidas(dimension, matrix, minX):
	distancias = {index +1: matrix[minX -1][index] for index in (range(dimension))}
	distanciasFilterZero = dict(filter(lambda x: x[1] > 0, distancias.items()))
	return min(distanciasFilterZero.items(), key = lambda x: x[1])

def getSucursalesIniciales(dimension, matrix, sucursales):
	minX = list(sucursales)[0]
	minimoPar = minimoConDemandasValidas(dimension, matrix, minX)
	minimo = minimoPar[1]
	minY = minimoPar[0]

	for i in sucursales:
		minimoPar = minimoConDemandasValidas(dimension, matrix, i)
		
		if (minimoPar[1] < minimo):
			minimo = minimoPar[1]
			minX = i
			minY = minimoPar[0]
	
	return minimo, minX, minY


def createOutput():
	capacidad, dimension, demandas, matrix = getData()

	sucursales =  {index + 1 for index in range(dimension)}

	secuencia = []

	print("Buscando dos primeras sucursales")
	minimo, minX, minY = getSucursalesIniciales(dimension, matrix, sucursales)

	print("La minima distancia es {} y pasa en X: {} e Y: {}".format(minimo, minX, minY))
	secuencia.append(minX)
	secuencia.append(minY)
	noVisitados = set(range(1,dimension + 1))
	noVisitados.remove(minX)
	noVisitados.remove(minY)

	print("Arranca procesamiento")

	while (len(secuencia) < dimension):
		print("Iteracion: {}".format(len(secuencia)))

		distancias = {index: matrix[secuencia[-1] - 1][index - 1] for index in noVisitados}
		distanciasFilterZero = dict(filter(lambda x: x[1] > 0, distancias.items()))
		minimoPar = min(distanciasFilterZero.items(), key = lambda x: x[1])
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