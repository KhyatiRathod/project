import csv
import math

item_file = []



with open('csv_file/groceries.csv','r') as file:
	read = csv.reader(file)

	for i in read:
		item_file.append(i)

# print(item_file)

min_support = 0.0022

threshold = math.ceil(min_support * len(item_file))
print(threshold)


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

i = 0
first = []
while(i<len(frequent_itemset)):
	if(frequent_itemset[i][1]>=threshold):
		first.append([frequent_itemset[i][0],frequent_itemset[i][1]])

	i=i+1
print(first)