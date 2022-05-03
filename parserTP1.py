import math

def getData(path):
	file1 = open(path,'r')

	lines = list(map(lambda x: x.strip(), file1.readlines()))
	file1.close()
	capacidad = int(lines[0].split(':')[1].strip())
	dimension = int(lines[1].split(':')[1].strip())

	indexCoordenadas = lines.index("NODE_COORD_SECTION")
	indexDemandas = lines.index("DEMANDAS")
	indexFinDemandas = lines.index("FIN DEMANDAS")

	i, j = dimension, dimension
	X = [0 for x in range(i)]
	Y = [0 for y in range(j)]
	dimensiones = [0 for x in range(i)]
	matrix = [[0 for x in range(i)] for y in range(j)]

	# CARGANDO DEMANDAS

	for i in range(indexDemandas + 1, indexFinDemandas, 1):
		line = lines[i].split(' ')
		dimensiones[int(line[0])-1]=int(line[1])

	# CARGANDO DISTANCIAS

	for i in range(indexCoordenadas + 1, len(lines) - 1,1):
		line = lines[i].split(' ')
		X[int(line[0]) - 1] = float(line[1])
		Y[int(line[0]) -1] = float(line[2])

	for i in range(len(X)):
		for j in range(len(Y)):
			if (i == j):
				matrix[i][j] = 0
			else:
				matrix[i][j] = math.sqrt(pow(X[i]-X[j],2) + pow(Y[i]-Y[j],2))

	return capacidad, dimension, dimensiones, matrix

