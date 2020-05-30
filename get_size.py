import os
import time
import sys


num = os.path.getsize(sys.argv[1]) #input is file loc
total = int(sys.argv[2]) #total file size, 81GB
print(num)
print(total)
time_df = 10 #seconds between update
t_remaining = 0
t = 0
while num < total:
	num2 = os.path.getsize(sys.argv[1])
	t+=10
	if num2 != num:
		v = (num2-num)/t #delta S/time
		t =0
		t_remaining = (total-num2)/v
		
		num = num2
		print("File Size: " + str(round(num/1000000000,3)) + "GB")
		print("Progress: " + str(round(num/total*100,3)) + "%")

		hrs = int(t_remaining/3600)
		mins = int((t_remaining/3600- hrs)*60)
		secs = int(((t_remaining/3600- hrs)*60 - mins)*60)

		#print("Time Remaining: " + str(round(t_remaining/3600,3)) + " hours")
		print("Time Remaining: " + str(hrs) + " hours, " + str(mins) + " mins, " + str(secs) + " seconds")
		print("****************")
	time.sleep(time_df)