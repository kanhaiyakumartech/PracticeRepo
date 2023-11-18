# This code for check and print duplicates elements in list

lis = [77, 82, 77, 22, 63, 84, 855, 77, 82, 22, 55, 6, 7, 88, 99, 99]

All_unique_List = []
Our_duplicate_List = []

for i in lis:
	if i not in All_unique_List:
		All_unique_List.append(i)
	elif i not in Our_duplicate_List:
		Our_duplicate_List.append(i)

print("these are Duplicate Element :",Our_duplicate_List)
