import math
import json
import sys

def createInputFiles():
	file1 = open(sys.argv[1],'r')
	lines = list(map(lambda x: x.strip(), file1.readlines()))
	file1.close()

	capacidad = int(lines[0].split(':')[1].strip())
	capacidadOut = open("capacidad.json",'w')
	json.dump(capacidad,capacidadOut)
	capacidadOut.close()
	
	dimension = int(lines[1].split(':')[1].strip())
	dimensionOut = open("dimension.json",'w')
	json.dump(dimension,dimensionOut)
	dimensionOut.close()

	indexCoordenadas = lines.index("NODE_COORD_SECTION")
	indexDemandas = lines.index("DEMANDAS")
	indexFinDemandas = lines.index("FIN DEMANDAS")

	i, j = dimension, dimension
	X = [0 for x in range(i)]
	Y = [0 for y in range(j)]
	demandas = [0 for x in range(i)]
	matrix = [[0 for x in range(i)] for y in range(j)]

	# CARGANDO DEMANDAS

	for i in range(indexDemandas + 1, indexFinDemandas, 1):
		line = lines[i].split(' ')
		demandas[int(line[0])-1]=int(line[1])

	demandasOut = open("demandas.json",'w')
	json.dump(demandas,demandasOut)
	demandasOut.close()
	
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

	matrixOut = open("matrix.json",'w')
	json.dump(matrix,matrixOut)
	matrixOut.close()

createInputFiles()