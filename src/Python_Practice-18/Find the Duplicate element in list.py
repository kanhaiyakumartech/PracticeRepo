
def Repeat_value(x):
	Size_list = len(x)
	repeated_values = []
	for i in range(Size_list):
		k = i + 1
		for j in range(k, Size_list):
			if x[i] == x[j] and x[i] not in repeated_values:
				repeated_values.append(x[i])
	return repeated_values
#we are passing a element in list
list_1 = [70, 80, 130, 40, 70, 80, 30,50, -200, 50, 740, 740, -60]
print (Repeat_value(list_1))
