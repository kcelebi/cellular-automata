import time
import copy
import random
import os

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

for j in range(5,1000):
	y,x = j,j
	direc =  str(x) + "x" + str(y)
	os.system('mkdir /Volumes/KayaHD/Projects/Cellular_Automata/' + str(direc))
	for i in range(1000):
		filend =  "_V" + str(i) + ".txt"
		filename = "/Volumes/KayaHD/Projects/Cellular_Automata/" + str(direc) + "/" + str(x) + "x" + str(y) + filend

		#print(str(x) + "x" + str(y) + filend + " : " + str(x*y/0.5*param/1000000) + "MB")
		mat = []
		for p in range(y):
			sub = [random.randint(0,1) for k in range(x)]
			mat.append(sub)

		f = open(filename,'a')
		for p in mat:
			f.write(str(p).replace("[","").replace("]","").replace(" ","") + "\n")
		f.close()

		#print(str(i/10) + "% Done for " + str(x) + "x" + str(y))
	print(str(j/995*100) + "% Done")
