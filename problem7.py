#breakfast choices
breakfast = ["Wheaties" , "Froot Loops" , "Cheerios", "Cap'n Crunch"]

def cereal_time():
#loop through entire list of choices and describe them as yummy
	for cereal in range(len(breakfast)):
		#if the cerel ends in an "s" print "are yummy" if not "is yummy"
		if breakfast[cereal][-1] == "s":
			print(breakfast[cereal],"are yummy!")
		else:
			print(breakfast[cereal],"is yummy!")
#call function
cereal_time()