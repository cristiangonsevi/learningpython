weight = float(input("Weight: "))
type = input("(K)g or (L)bs: ")

if type == 'k' or type == 'K':
	print(f"Weight in Lbs: {weight * 2.2}")
elif type == 'l' or type == 'L':
	print(f"Weight in kg: {weight / 2.2}")
