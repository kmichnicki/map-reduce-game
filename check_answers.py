from the_game import *
from map_reduce_game import *
import random
import numpy as np

data = []
for i in range(1000):
    data.append(random.randint(0,100))


temp = households(data, Minions())
if (len(data) == temp[0]):
    print "You got the total number of households right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong number of households :'("
print "\n"

temp = total(data, Minions())
if (sum(data) == temp[0]):
    print "You got the total population right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong total population :'("
print "\n"

temp = average(data, Minions())
if (1.0*sum(data)/len(data) == temp[0]):
    print "You got the average number of people per household right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong average number of people per household :'("
print "\n"

avg = 1.0*sum(data)/len(data)
variance = 1.0*sum(map(lambda x: (x - avg)**2, data)) / (len(data) - 1)
std = np.sqrt(variance)
temp = standard_deviation(data, Minions())
if (std == temp[0]):
    print "You got the standard deviation of the number of people per household right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong standard deviation of the average number of people per household :'("
print "\n"

temp = maximum(data, Minions())
if (max(data) == temp[0]):
    print "You got the number of people in the most populated house right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong number of people in the most populated house :'("
print "\n"

temp = minimum(data, Minions())
if (min(data) == temp[0]):
    print "You got the number of people in the least populated house right!"
    print "It took you " + str(temp[1]) + " rounds to do it."
else:
    print "You got the wrong number of people in the least populated house :'("
