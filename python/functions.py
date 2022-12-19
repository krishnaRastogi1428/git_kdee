def gmean(a, b):
	mean = (a*b)/(a+b)
	print (mean)

def isGreater(a, b):
	if(a > b):
		print ("first is greater")
	
	else:
		print("second is greater")

a = 100000000
b = 1100
gmean(a, b)
isGreater(a, b)