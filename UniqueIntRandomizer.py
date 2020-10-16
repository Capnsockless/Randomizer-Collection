import random
import json
import ast
import os

os.chdir("D:\Randomizers")

def open_json(jsonfile):		#open function for jsonfiles
	with open(jsonfile, "r") as fp:
		return json.load(fp)

def save_json(jsonfile, name):	#save function for jsonfiles
	with open(jsonfile, "w") as fp:
		json.dump(name, fp)


#This function generates random numbers and stores them into a jsonfile, it always generates a number that isn't already present.
#When the amount of numbers reaches a certain fraction (which is determined by the delafter argument) the first delfraction fraction
#of the total amount is deleted to clear space and allow the numbers which appeared long ago to have a chance to generate again.
def unique_int_randomizer(length, delafter: float, delfraction):
	if delafter >= 1 or delafter <= 0:
		print("delafter argument must be between 0 and 1.")
	elif delfraction < 1:
		print("delfraction argument must be 1 or greater than 1.")
	else:
		intdict = open_json("UniqueIntRandomizer.json")			#the json file can be an argument of the function if multiple are used
		numlist = ast.literal_eval(intdict["usednumbers"])			#convert list(which is presented as a string) to a python list
		if len(numlist) > length*delafter:			#if amount of stored numbers surpasses given fraction of the total amount delete a chunk of the numbers at the start
			del numlist[:round(length/delfraction)]		#amout of numbers to delete is the argument delfraction
			save_json("UniqueIntRandomizer.json", intdict)
		while True:			#keep generating new numbers
			n = random.randint(0, length)
			if n not in numlist:		#get a number that isn't already used and append it to the list of numbers in use
				numlist.append(n)
				intdict["usednumbers"] = str(numlist)		#convert list back to a "jsonlist"(a string which resembles a list) and save it
				save_json("UniqueIntRandomizer.json", intdict)
				return n

randomint = unique_int_randomizer(100, 0.8, 4)
print(randomint)
