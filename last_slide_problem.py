original_list = ["oranges", "apples", "pears", "bananas"]

def reverse_list(original_list):
	#create blank list to populate the reversal
	reversed_list = []
	#loop through list 
	for fruit in range(len(original_list)):
		#append the reversal
		reversed_list.append(original_list[len(original_list) - fruit - 1])
	return reversed_list

my_new_list = reverse_list(original_list)
print(my_new_list)