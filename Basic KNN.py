import math
ClassA = [(1,1), (2,1), (4,1), (2,2), (1,2.5)]
ClassB = [(3,1), (3, 1.5), (3, 2.5), (4,4), (2,4)]

tstPts = [(3.8, 1.2), (1.2, 3.2), (4, 3.2)]

k= [1, 3, 5] 

def distanceFormula(pt1,pt2):
	return math.sqrt( (pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )

def findClosestPoints(point, k):

	distances = []

	for pt in ClassA:
		distances.append((distanceFormula(pt, point), "ClassA"))
	for pt in ClassB:
		distances.append((distanceFormula(pt, point), "ClassB"))

	finalDistances = []

	distances = sorted(distances, key = lambda x: x[0])

	for i in range(0, k):
		finalDistances.append(distances[i])

	return finalDistances

def KNN(pt, k):
	closestDistance = findClosestPoints(pt,k)

	seenClassA = 0
	seenClassB = 0;

	for neighbor in closestDistance:
		if(neighbor[1] == "ClassA"):
			seenClassA = seenClassA + 1
		else:
			seenClassB = seenClassB + 1


	if(seenClassA > seenClassB):
		return "Class A"
	else:
		return "Class B"



for pt in tstPts:
	for i in range(0, 3):
		print(str(pt) + " is " + KNN(pt, k[i]) + " when using " + str(k[i]) + " neighbors")