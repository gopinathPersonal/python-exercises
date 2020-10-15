def busyStudent(startTime, endTime, queryTime):
		count = 0
		for i in range(0,len(startTime)):
			for j in range(0,len(endTime)):
				if(i == j):
					if (queryTime >= startTime[i] and queryTime <= endTime[j]):
						count = count + 1
					break
		return count

result = busyStudent([9,8,7,6,5,4,3,2,1], [10,10,10,10,10,10,10,10,10], 5)
print(result)