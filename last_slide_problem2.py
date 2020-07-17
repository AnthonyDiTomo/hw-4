original_list = ["oranges", "apples", "pears", "bananas"]

#create blank list to populate the reversal
reversed_list = []
#loop through list 
for i in range(len(original_list)):
	#append the reversal
	reversed_list.append(original_list[len(original_list) - 1 - i])
print(reversed_list)

#0
# reversed_list = ['bananas']
#1
#
#2
#3