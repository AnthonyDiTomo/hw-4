user_entry = input("what is your favorite color?: ")
answer = ""
#set i to reference the last index in the string
i = len(user_entry)-1
#loop through the string starting at the end to generate the answer
while i>= 0:
	answer = answer + user_entry[i]
	#set the increments for the loop
	i -= 1
print(answer)