import time
import copy
import random
import os

filend = "ca.txt"
y,x = 100, 100
param = 10

#filename = "/Volumes/KayaHD/Projects/Cellular_Automata/" + str(x) + "x" + str(y) + filend
filename = '/Users/kayacelebi/Projects/Cellular_Automata/Full_Files/' + str(x) + "x" + str(y) + "x" +str(param) + filend
print(str(x) + "x" + str(y) + filend + " : " + str(x*y/0.5*param/1000000) + "MB")
mat = []
for p in range(y):
	sub = [random.randint(0,1) for k in range(x)]
	mat.append(sub) 

#preset coords
#mat[5][4],mat[5][5],mat[5][6],mat[4][5] = 1,1,1,1

tempmat = copy.deepcopy(mat)
i= 0


def in_range(arr):
	if arr[0] < y and arr[0] > -1 and arr[1] > -1 and arr[1] < x:
		return True
	return False

def display_array(mat):
	#y = len(mat)
	#x = len(mat[0])
	newmat = []
	for p in range(y):
		sub = [0]*x
		newmat.append(sub)

	for y_ in range(y):
		for x_ in range(x):
			if mat[y_][x_] == 1:
				newmat[y_][x_] = "███"
			else:
				newmat[y_][x_] = "   "

	print(" " + "".join(["----" for x in range(x)]))
	for y_ in range(y):
		print("|" + " ".join(newmat[y_]) + "|")
	print(" " + "".join(["----" for x in range(x)]))

#display_array(mat)
f = open(filename,'w')
while i < param:
	for y_ in range(y):
		for x_ in range(x):
			curr = [y_,x_]
			neighbors = [
					[curr[0]+1,curr[1]+1],
					[curr[0]+1,curr[1]],
					[curr[0]+1,curr[1]-1],
					[curr[0],curr[1]+1],
					[curr[0],curr[1]-1],
					[curr[0]-1,curr[1]+1],
					[curr[0]-1,curr[1]],
					[curr[0]-1,curr[1]-1]
					]
			alive = 0
			for n in neighbors:
				if in_range(n): 
					alive += mat[n[0]][n[1]]
			if mat[y_][x_] == 1 and (alive <2 or alive >3): #if cell alive, dies condition
				tempmat[y_][x_] = 0
			elif mat[y_][x_] == 0 and alive == 3:
				tempmat[y_][x_] = 1

	
	mat = copy.deepcopy(tempmat)
	f = open(filename,'a')
	for p in mat:
		f.write(str(p).replace("[","").replace("]","").replace(" ","") + "\n")
	#f.write("-\n")
	#f.close()
	#display_array(mat)
	#time.sleep(0.5)
	i+=1

#subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python', str(filename) + ' ' + str(x*y/0.5*param/1000000), 'get_size.py'])

#os.system('python3 get_size.py ' + str(filename) + ' ' + str(x*y/0.5*param/1000000)) #run 2nd program

os.system('processing-java --sketch=/Users/kayacelebi/Projects/Cellular_Automata/code/automata --run') 
