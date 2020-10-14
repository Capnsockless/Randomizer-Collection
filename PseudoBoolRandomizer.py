import random
import statistics

#If we roll dice n times, then every next roll would determine True or False depending on if
#the latest rolled number is in the previous n amount of numbers. This creates a pseudorandomizer
#which has a greater chance of being True after multiple False's like so: (if n = 4)
#if we have 1, 2, 3, 4 as previous numbers chance of True is 1/3(2/6), if we get a False,
#and have 2, 3, 4, 3 as previous numbers now the chance of True is 1/2(3/6). This system is flawed
#since if the latest number is the last number the chance of True doesn't increase.

#Generates 100 booleans with the above mentioned "algorithm", you can set the variables
#dicesides(the amount of sides the dice has) and nrolls(the amount of previous numbers we're comparing the new number to)
#to change the odds however you would like to see
def bool_generator(dicesides, nrolls, n=0):
    if dicesides <= 0 or type(dicesides) != int:        #dicesides and nrolls must be natural numbers
        print("dicesides must be a natural integer.")
    elif nrolls <= 0 or type(nrolls) != int:
        print("nrolls must be a natural integer.")
    else:
        dicenumbers = [random.randint(1,dicesides) for _ in range(100 + nrolls)]    #generates 100+nroll random numbers of the dice sides
        dicebooleans = []
        for i in dicenumbers:           #sets the booleans with the "algorithm"
            if dicenumbers[i] in dicenumbers[n-nrolls:n]:
                dicebooleans.append(False)
            else:
                dicebooleans.append(True)
            n += 1
        del dicebooleans[:nrolls]   #delete the first nrolls amount of booleans since they're not useful as stats
        return dicebooleans

#I noticed this can also be used for a moderately predictable percent randomizer if we generate 100 booleans
#the average of possible percentages can be managed by setting certain dicesides and nrolls
def random_percent(booleans):
    return booleans.count(True)/len(booleans)

#Generates 50 random percents with the given dicesides and nrolls
def multiple_percent(dicesides, nrolls):
    if dicesides <= 0 or type(dicesides) != int:        #dicesides and nrolls must be natural numbers
        print("dicesides must be a natural integer.")
    elif nrolls <= 0 or type(nrolls) != int:
        print("nrolls must be a natural integer.")
    else:
        listofpercents = []
        for _ in range(50):
            pseudobools = bool_generator(dicesides, nrolls)
            listofpercents.append(random_percent(pseudobools))
        return listofpercents

print("Pseudorandom booleans: ", bool_generator(6, 4))
print("Random percentages: ", multiple_percent(6, 4))
print("Average percent: ", statistics.mean(multiple_percent(6, 4)))
print("Variance: ", statistics.variance(multiple_percent(6, 4)))
