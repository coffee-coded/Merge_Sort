import re


def mergesort(list):
	new_list = []
	if len(list) == 1:
		return list
	elif len(list) == 2:
		if list[0]>list[1]:
			new_list.append(list[1])
			new_list.append(list[0])
		else:
			new_list.append(list[0])
			new_list.append(list[1])
		return new_list
	else:
		if len(list)%2==0:
			first_half = mergesort(list[:int(len(list)/2)])
		else:
			first_half = mergesort(list[:int(len(list) / 2)+1])
		second_half = mergesort(list[len(list)-int(len(list)/2):])
		running = True
		while(running):
			if len(first_half)!=0 and len(second_half)!=0:
				if first_half[0]<=second_half[0]:
					new_list.append(first_half[0])
					del first_half[0]
				else:
					new_list.append(second_half[0])
					del second_half[0]
			elif len(first_half)!=0 and len(second_half)==0:
				new_list.append(first_half[0])
				del first_half[0]
			elif len(first_half)==0 and len(second_half)!=0:
				new_list.append(second_half[0])
				del second_half[0]
			elif len(first_half)==0 and len(second_half)==0:
				running = False
				break
		return new_list


print("Press q to quit inserting values\n")
list = []
i = 0
while(True):
	x = input("Input : ")
	if x == "q" or x == "Q":
		break
	else:
		x = re.sub('[a-zA-Z,:()" "]','', x)
		if len(x) != 0:
			print("Your input of ",x,"has been added")
			list.insert(i,int(x))
			i+=1
		else:
			print("Couldn't be added")
print("Unsorted List : ",end="")
print(list)
print(" Sorted  List : ",end="")
print(mergesort(list))
