import parserTP1 as parser

capacidad, dimension, demandas, matrix = parser.getData("problema_uno.txt")

acum = 0
lists = [list() for i in range(dimension)]

for i in range(dimension):
	acum = 0
	visitados = []
	j = 1
	visitados.append(i + 1)
	lists[i].append(i + 1)
	while (len(visitados) < 150):
		if ((j not in visitados) 
			and (acum + demandas[j - 1] >= 0) 
			and (acum + demandas[j - 1] <= 30)
			and (j <= 150)):
			lists[i].append(j)
			acum += demandas[j - 1]
			visitados.append(j)
		j += 1

		if ((len(visitados) < 150) and (j > 150)):
			j = 1

distancias=[]
for i in range(len(lists)):
	acum = 0
	for j in range(len(lists) - 1):
		acum += matrix[lists[i][j] - 1][lists[i][j+1] - 1]
	distancias.append(acum)

minDistancia = min(distancias)
nroIteracion = distancias.index(minDistancia)
print("La minima distancia es {} y paso en la iteracion numero {}".format(minDistancia, nroIteracion))

fileOut = open("output.txt",'w')
for i in range(len(lists[nroIteracion])):
	fileOut.write("{} ".format(lists[nroIteracion][i]))
fileOut.close()
