import re, time

#TODO remake findNextClass

def nearAssignment(assignments):
        near = ''
	r = ''
        for x in range(len(assignments)):
                tmp = assignments[x][2]
                if near == '':
                        near = tmp
			r = assignments[x][0]+' '+assignments[x][2]
                elif near[0:4] == tmp[0:4]:
                        if near[5:7] == tmp[5:7]:
                                if near[8:10] > tmp[8:10]:
                                        #if tmp[8:10] >= time.strftime("%d"):
                			r = assignments[x][0]+' '+assignments[x][2]  
		                        near = tmp
        return r

def findNextClass(H):
	horario = H
	day = time.strftime("%A")
	nextHour = '10' #str(int(time.strftime("%H"))+1)
	hcount = 0
	near = '24'
	dias = ['Lunes','Martes','Miercoles','Jueves','Viernes']
	horas = ['8','9','10','11','12','13','14','15','16','17','18','19','20']
	for w in range(len(horas)):
		m = re.search(horas[w], horario)
     		if m != None:
        		hcount += 1
	aux = horario.split('},"',hcount)
	aux[hcount-1] = aux[hcount-1][:len(aux[hcount-1])-1]
	for q in range(len(aux)):
		aux[q] = re.split(",",aux[q])
		m = re.match(r"(.*?)\":\{(\"(.*?)\":\"(.*?)\")",aux[q][0])
		aux[q][0] = m.group(2)
		aux[q].append(m.group(1))
	for x in horas:
		for y in range(len(aux)):
			t = re.search(x,aux[y][len(aux[y])-1])
			if t != None:
				row = []
				row.append(x)
                        	for z in dias:
                        		for d in range(len(aux[y])-1):                          
						dayPattern = re.compile(r"\"(.*?)\":\"(.*?)\"")
						t = dayPattern.match(aux[y][d])
						if t.group(1) == z:
							if day == z and int(nextHour) <= int(x): 
								return t.group(2)
	return "Proximo dia"
