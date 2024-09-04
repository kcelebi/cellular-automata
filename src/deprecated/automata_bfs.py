import copy
import random as r
import automata

def in_range(arr):
	if arr[0] < dimx and arr[0] > -1 and arr[1] > -1 and arr[1] < dimy:
		return True
	return False

dimx = 10
dimy = 10
mat = [ [r.randint(0,1) for j in range(dimx)] for i in range(dimy)]
tempmat = copy.deepcopy(mat) #make array that takes changes


#bfs
for i in range(1000):
	vis = [] #visited
	q = [] #queue
	q.append([1,1]) #first coord
	vis.append([1,1])
	t = 1
	while len(q) > 0:
		curr = q[0]
		#print(curr)
		q.remove(curr)
		if curr not in vis or t == 1:
			t=0 #just to start it off
			vis.append(curr)
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
					q.append(n)
					if tempmat[n[0]][n[1]] == 1: alive +=1

			if tempmat[curr[0]][curr[1]] == 1 and (alive < 2 or alive > 3): #if cell alive, dies condition
				tempmat[curr[0]][curr[1]] = 0
			elif tempmat[curr[0]][curr[1]] == 0 and alive == 3:
				tempmat[curr[0]][curr[1]] = 1
		
		#automata.display_array(tempmat)
		#print("----------")

mat = copy.deepcopy(tempmat)# assign temp to mat to finalize changes