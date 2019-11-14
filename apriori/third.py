import csv
import math

item_file = []



with open('groceries.csv','r') as file:
	read = csv.reader(file)

	for i in read:
		item_file.append(i)

# print(item_file)

min_support = 0.0022

threshold = min_support * len(item_file)
print(math.ceil(threshold))


itemset = []
i=0

while(i<len(item_file)):
	k=0
	while(k<len(item_file[i])):
		if(item_file[i][k] not in itemset):
			itemset.append(item_file[i][k])
		k=k+1
	i=i+1

# print("\n","\n",itemset,len(itemset))

# ------------------------------ first round ---------------------------------------------------
frequent_itemset = []

for i in itemset:
	count = 0
	j = 0
	while( j < len(item_file)):
		h = 0

		while(h < len(item_file[j])):
			if(item_file[j][h] == ''):
				break
			elif(item_file[j][h] == i):
				count = count + 1
			h=h+1
		j=j+1
	frequent_itemset.append([i,count])
# print ("\n","\n",frequent_itemset,"\n","\n")

i = 0
first = []
while(i<len(frequent_itemset)):
	if(frequent_itemset[i][1]>=threshold):
		first.append([frequent_itemset[i][0],frequent_itemset[i][1]])

	i=i+1
# print(first)

# ------------------------------ second round -------------------------------------------------

i = 0
second = []

while (i < len(frequent_itemset)):
	item1 = frequent_itemset[i][0]
	j = 1
	while (j < (len(frequent_itemset)-1)):
		item2 = frequent_itemset[j][0]
		if(item1 != item2):
			k = 0
			count = 0
			while(k<len(item_file)):
				if(item1 in item_file[k]):
					if(item2 in item_file[k]):
						count = count + 1
						if(len(second)==0):
							second.append([item1,item2,count])
						else:

							p = len(second)-1
							while (p >=0 ):
								if (second[p][0] == item1):
									if(second[p][1]==item2):
										second[p][2] = second[p][2] + 1
								elif(second[p][1] == item1):

									if(second[p][0] == item2):
										second[p][2] = second[p][2] + 1
								else:
									second.append([item1,item2,count])
								p=p-1
				k=k+1
		j=j+1
	i=i+1

p = 0
while(p < len(second)):
	if(second[p][2]<threshold):
		second.remove(second[p])
	p=p+1

# print ("\n\n\n",second)


# ----------------------------------- third round -------------------------------------------------

third = []


while (i < len(frequent_itemset)):
	item1 = frequent_itemset[i][0]
	j = 1
	while (j < (len(frequent_itemset)-1)):
		item2 = frequent_itemset[j][0]
		if(item1 != item2):
			h = 0
			while (h < (len(frequent_itemset)-2)):
				item3 = frequent_itemset[h][0]
				if(item2 != item3 and item1 != item3):
					k = 0
					count = 0
					while(k<len(item_file)):
						if(item1 in item_file[k]):
							if(item2 in item_file[k]):
								if(item3 in item_file[k]):
									count = count + 1
									if(len(third)==0):
										third.append([item1,item2,item3,count])
									else:
										p = len(third)-1
										while (p >=0 ):
											if (third[p][0] == item1):
												if(third[p][1]==item2):
													if(third[p][2] == item3):
														third[p][3] = third[p][3] + 1
											elif(third[p][1] == item1):
												if(third[p][2] == item2):
													if(third[p][0] == item3):
														third[p][3] = third[p][3] + 1
											elif(third[p][2] == item1):
												if(third[p][0] == item2):
													if(third[p][1] == item3):
														third[p][3] = third[p][3] + 1
											elif(third[p][1] == item1):
												if(third[p][0] == item2):
													if(third[p][2] == item3):
														third[p][3] = third[p][3] + 1
											elif(third[p][0] == item1):
												if(third[p][2] == item2):
													if(third[p][1] == item3):
														third[p][3] = third[p][3] + 1
											elif(third[p][2] == item1):
												if(third[p][1] == item2):
													if(third[p][0] == item3):
														third[p][3] = third[p][3] + 1

											else:
												third.append([item1,item2,item3,count])
											p=p-1
						k=k+1
				h=h+1
		j=j+1
	i=i+1

p = 0
while(p < len(second)):
	if(second[p][3]<threshold):
		second.remove(second[p])
	p=p+1

print("\n\n\n",third)
