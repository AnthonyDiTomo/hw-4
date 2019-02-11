#breakfast choices
breakfast = ["Wheaties" , "Froot Loops" , "Cheerios", "Cocoa Krispies"]

def cereal_time():
#loop through entire list of choices and describe them as yummy
	for cereal in range(len(breakfast)):
		print(breakfast[cereal],"are yummy!")
#call function
cereal_time() 