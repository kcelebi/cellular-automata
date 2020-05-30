import copy
import time

def in_range(arr):
	if arr[0] < 10 and arr[0] > -1 and arr[1] > -1 and arr[1] < 10:
		return True
	return False

def display_array(mat):
	y = len(mat)
	x = len(mat[0])
	newmat = [[0]*x]*y

	for y_ in range(y):
		for x_ in range(x):
			if mat[y_][x_] == 1:
				newmat[y_][x_] = "█"
			else:
				newmat[y_][x_] = " "
	for y_ in range(y):
		print("".join(newmat[y_]))

#preset coords
mat = [[0]*10]*10
mat[5][5],mat[5][6],mat[4][5],mat[4][6] = 1,1,1,1

tempmat = copy.deepcopy(mat) #make array that takes changes

vis = [] #visited
q = [] #queue
q.append([5,5]) #first coord
vis.append([5,5])
t = 1

#bfs
while len(q) > 0:
	curr = q[0]
	#print(curr)
	q.remove(curr)
	if curr not in vis or t == 1:
		t=0 #just to start it off
		vis.append(curr)
		#print("Curr: " + str(curr[0]))
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
		#print("Neighbors: " + str(neighbors))
		alive = 0
		for n in neighbors:
			if in_range(n):
				q.append(n)
				if tempmat[n[0]][n[1]] == 1: alive +=1

		#print("Alive: " + str(alive))
		#print("Dead: " + str(8-alive))
		if tempmat[curr[0]][curr[1]] == 1 and (alive <2 or alive >3): #if cell alive, dies condition
			tempmat[curr[0]][curr[1]] = 0
		elif tempmat[curr[0]][curr[1]] == 0 and alive == 3:
			tempmat[curr[0]][curr[1]] = 1
	display_array(tempmat)
	print("----------")
	time.sleep(0.2)

mat = copy.deepcopy(tempmat)# assign temp to mat to finalize changes