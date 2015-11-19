import re, urllib2

response = urllib2.urlopen('http://raiblax.com/pbe/receptor.php?id_alumno=gonzalo.polo')
datos = response.read()
print datos
tareas = re.compile("tareas")
horario = re.compile("horario")
notas = re.compile("NOTAS")
x = tareas.search(datos)
y = horario.search(datos)
z = notas.search(datos)
tareas = datos[x.start()+9:y.start()-4]
horario = datos[y.start()+11:z.start()-2]
notas = datos[z.start()+6:len(datos)-1]
print horario
print '--------------------------'
#print notas
#print '--------------------------'
#print tareas
#print '--------------------------'
hcount = 0
dias = ['Lunes','Martes','Miercoles','Jueves','Viernes']
horas = ['8','9','10','11','12','13','14','15','16','17','18','19','20']
for w in range(len(horas)):
	m = re.search(horas[w], horario)
        if m != None:
        	hcount += 1
aux = horario.split('},"',hcount)
print aux[0]
print '--------------------------'
aux[hcount-1] = aux[hcount-1][:len(aux[hcount-1])-1]
print aux
print '--------------------------'
for q in range(len(aux)):
	aux[q] = re.split(",",aux[q])
	m = re.match(r"(.*?)\":\{(\"(.*?)\":\"(.*?)\")",aux[q][0])
	aux[q][0] = m.group(2)
	aux[q].append(m.group(1))
print aux
print '--------------------------'
for x in horas:
	for y in range(len(aux)):
		t = re.search(x,aux[y][len(aux[y])-1])
		if t != None:
			row = []
			row.append(x)
                        for z in dias:
                        	for d in range(len(aux[y])-1):
                                	#print "aux[y][d] "+aux[y][d]
					dayPattern = re.compile(r"\"(.*?)\":\"(.*?)\"")
					tmp = re.split(":",aux[y][d])
					t = dayPattern.match(aux[y][d])
					print t.group(1)
					if t.group(1) == z:
						row.append(t.group(2))
						break
					if d == len(aux[y])-2:
						row.append("---")
					#print t.group(2)
					#t = re.search(z,tmp[0])
					#row.append(aux[y][d][t.end()+3:len(aux[y][d])-2])
			print '--------------------------'
			print row 
