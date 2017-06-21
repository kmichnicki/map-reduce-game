
"""
Welcome to the Map Reduce Game! You are the great ruler of a great city. You would like to perform a census of your city. You have a list of data, one row per household. Each row is a number representing the number of people in that household. The point of the game is to do calculations using your minions for memory. That is, you create minions, assign values to them and get values from them. The only problem is that your minions are kind of dumb. They can only remember one number. That number can never change, i.e. it can only be assigned once. The minions also can only tell you the value once per round. You cannot assign and get a value in the same round.

The point of the game is to illustrate how parallel processing works. Everything that you do in a single round, a cluster of computers could do in a constant amount of time. Thus the number of rounds corresponds to the amount of time it would take a cluster of computers to do the calculation. 

1. New Minions. You can spawn a minion to your horde using `horde.add_minion()`. Your horde will contain on minion initially. This minion should only be assigned to in the final round for he is the minion who reports the final answer. 

2. Assigning Values. You can assign a value to a minion using the `assign` method. For instance, if you wanted to assign a value x to minion n you would call `horde.assign(n, x)`. Each value can be assigned only once per minion. If you need to assign a new number, you need to create a new minion. You cannot assign and read in the same round. 

3. Getting Values. You can get a value from a minion using the `get` method. For intstance, if you wanted the value from the nth minion, you would call `horde.get(n)`. You can only read each value once per round which means at most twice per minion per round. 

4. New Round. In order to be able to get a value once it has already been read(or after a minion has been assigned to), you must start a new round. You do this with the `new_round` method with the following code `horde.new_round()`. The game starts at round 0 and each time `new_round` is called, it adds 1 to the number of rounds. 

5. Current round. You can see what the current round is by calling `horde.current_round()`


Fill in the following functions:
"""

def households(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
  
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 
    # 1 minion initially. 
    horde.assign(0, len(data))
    horde.next_round()

    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the answer, the current round, number of minions

def total(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
    
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 

    for i, row in enumerate(data):
        horde.spawn_minion()
        if (i == 0):
            horde.assign(i+1, row)
        else:
            horde.assign(i+1, row + horde.get(i))
        horde.next_round()

    horde.assign(0, horde.get(len(data)))
    horde.next_round()
    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the current value and the current round

def average(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
    
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 

    horde.assign(0, 0)
    horde.next_round()

    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the answer, the current round, number of minions

def standard_deviation(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
    
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 

    horde.assign(0, 0)
    horde.next_round()

    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the answer, the current round, number of minions

def maximum(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
    
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 

    horde.assign(0, 0)
    horde.next_round()

    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the answer, the current round, number of minions

def minimum(data, horde):
    """
    data: a list of integers. Each integer represents the number of people in a household. 
    horde: this is the object that you will use in order to spawn, assign values to and get values from your minions. Instructions are above. 
    """
    # count the total number of households in the city using a minimum of rounds
    # store the final answer using the first number of the first minion. 
    
    horde.spawn_minion() # the first minion will report the final value. Don't assign a value to this minion until the very end.  
    ### new code starts here. There should be no new lines of code above this line. 

    horde.assign(0, 50)
    horde.next_round()

    ### new code ends here. There should be no new lines of code below this line. 
    return (horde.get(0), horde.current_round(), horde.size_of_horde()) # returns a tuple with the answer, the current round, number of minions
   
