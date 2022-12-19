AS_numerator = input("Enter numerator(of aspect ratio): ")

AS_denominator = input("Enter denominator(of aspect ratio): ")

lowerRes = input("Enter vertical component: ")
print("Aspect Ratio = ", AS_numerator, ":", AS_denominator)

for lower in range(1, int(lowerRes)+1):
	upper = (int(AS_numerator) * int(lower)) / int(AS_denominator)
	if(upper == int(upper)):
		print(int(upper), "x", lower)

input()
