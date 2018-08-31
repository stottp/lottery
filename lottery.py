#!/usr/bin/env python
import random
import math
from datetime import date

weeks = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')

def choose_lottery_numbers(game="lotto", lines=1):
    """ Returns numbers based on game and the number of lines""" 
    if game == 'lotto':
        return lotto(lines) 
    if game == 'euromillions':
        return euromillions(lines) 
    if game == 'lotto_hotpicks':
        return lotto_hotpicks(lines)
    if game == 'euro_hotpicks':
        return euro_hotpicks(lines)
    if game == 'thunderball':
        return thunderball(lines) 
        
def calculate_lottery_costs(*games):
    """ Calculates the cost of playing the lottery"""
    cost = 0
    for game in games:
        if game == 'lotto':
            cost += 2.00 
        if game == 'euromillions':
            cost += 2.00  
        if game == 'lotto_hotpicks':
            cost += 2.00 
        if game == 'euro_hotpicks':
            cost += 2.00 
        if game == 'thunderball':
            cost += 2.00
    print 
    return cost
         
def lotto(lines = 1):
    """ Choose 6 numbers between 1 to 59"""
    return [sorted(random.sample(range(1,60), 6)) for _ in range(lines)]
    
def euromillions(lines = 1):
    """ Choose 5 numbers between 1 to 50 and 2 lucky stars between 1 to 12"""
    return [(sorted(random.sample(range(1,51), 5)), sorted(random.sample(range(1,13), 2))) for _ in range(lines)]

def lotto_hotpicks(lines = 1):
    """ Choose 5 numbers between 1 to 59"""
    return [sorted(random.sample(range(1,60), 5)) for _ in range(lines)]
    
def euro_hotpicks(lines = 1):
    """ Choose 5 numbers between 1 to 50"""
    return [sorted(random.sample(range(1,51), 5)) for _ in range(lines)]
    
def thunderball(lines = 1):
    """ Choose 5 numbers between 1 to 39 and 1 Thunderball between 1 to 14"""
    return [(sorted(random.sample(range(1,40), 5)), sorted(random.sample(range(1,15), 1))) for _ in range(lines)]    
     
print 'Lottery draw for {}'.format(weeks[date.today().weekday()])
print choose_lottery_numbers('euromillions', lines = 2)
print choose_lottery_numbers('thunderball', lines = 2)
#print choose_lottery_numbers('lotto', lines = 2)
#print choose_lottery_numbers('thunderball', lines = 2)

# If day then do this 

#print math.factorial(59)/(math.factorial(59-6)*math.factorial(6))
#print math.factorial(39)/(math.factorial(39-5)*math.factorial(5)) * math.factorial(14)/(math.factorial(14-2)*math.factorial(2))
