"""
    Compute and solve Blackout Math problems

   author: Lindsay Martinescu
   revised: September 2014
"""
import re

def compute(str1):
    """
        Takes a string and splits into values and operators
        If only one value, returns that value
        If no values, returns None
        If trys to parse empty value, returns None (two ops in a row)
        Otherwise evaluates operators and values and returns result 
    """
    firstdigit = None
    lastdigit = None
    values = []
    operators = []
    for c in range (len(str1)):
        if str1[c].isdigit() and firstdigit == None:
            firstdigit = c
        if not str1[c].isdigit(): 
            lastdigit = c
        if firstdigit != None and lastdigit != None:
            st = str1[firstdigit:lastdigit]
            if st == "":
                return None
            values += [int(str1[firstdigit:lastdigit])]
            operators += [str1[c]]
            firstdigit = None
            lastdigit = None
        if firstdigit != None and c == len(str1)-1:
            values += [int(str1[firstdigit:])]
    
    if len(values) == 1:
        return values[0]
    if len(values) == 0:
        return None
    values.reverse()
    operators.reverse()
    firstval= values.pop()
    while len(values) > 0:
        op = operators.pop()
        secondval = values.pop()
        firstval = docalc(firstval,secondval,op)
    
    return firstval 

def docalc(firstval,secondval,op):
    """
        Takes in string of operators and does the proper operation
    """
    if op == "*" or op == "x":
        return firstval * secondval
    if op == "/":
        return firstval / secondval
    if op == "+":
        return firstval + secondval
    if op == "-":
        return firstval - secondval
    
def evaluate(puzzle):
    """
        Checks to make sure puzzle parts are not = to None
        Also checks that parts are equal to each other
    """
    pieces = puzzle.split("=")
    ans1 = compute(pieces[0])
    ans2 = compute(pieces[1])
    return ans1 != None and ans2 != None and ans1 == ans2

def solve(puzzle):
    """
        Checks to make sure if there is more than one equal sign
        Only will check first two parts
        Solve the puzzle and blackout numbers
        Return No solutions found if not valid 
    """
    pieces = puzzle.split("=")
    if evaluate(pieces[0] + "=" + pieces[1]):
        return pieces[0] + "=" + pieces[1]
    for c in range(len(pieces[0])):
        if pieces[0][c].isdigit():
            temp = pieces[0][:c] + pieces[0][c+1:]
            for x in range(len(pieces[1])):
                if pieces[1][x].isdigit():
                    temp2 = pieces[1][:x] + pieces[1][x+1:]
                    temppuzzle = temp + "="+ temp2
                    if evaluate(temppuzzle):
                        return temppuzzle
    return "No Solution Found"

def validatePuzzle(puzzle):
    """
        Searches string for proper characters
        If invalid characters found will return None
    """
    return re.search("[^0-9*x/+-=]",puzzle)== None
    

def main():
    puzzle = input("Insert whole puzzle")
    if validatePuzzle(puzzle):
        print(solve(puzzle))
    else:
        print("Invalid Input")
    
main()

