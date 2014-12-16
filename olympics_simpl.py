"""
   Sort through a list of Olympians
   Output number of gold medals for a specific year
   Output gold, bronze, and silver medals for specific Olympian

   author: Lindsay Martinescu
   revised: September 2014
"""

def findGold(yearFind):
    """
        Starts total= to zero
        Reads each line of file one at a time
        Looks for year and first place medals
        Every time there is a 1, gold medal, it adds to total
        returns total
    """
    total = 0
    with open('athletes.txt', mode='r',encoding='UTF-8') as f:
        while True:
            lastname = f.readline().strip()
            firstname = f.readline().strip()
            year = f.readline().strip()
            postion =f.readline().strip()
            if postion == '1' and year== yearFind:
                total= total+1
            if not f.readline():
                break
    return total

def medalsForPerson(first,last):
    """
        Starts all total= to zero
        Reads each line of file one at a time
        Looks for name inputted and medals won by person
        Every time there is a 1,2,3 for a person, adds to total
        Returns total for each medal type
    """
    goldTotal = 0
    silverTotal = 0
    bronzeTotal = 0
    with open('athletes.txt', mode='r',encoding='UTF-8') as f:
        while True:
            lastname = f.readline().strip()
            firstname = f.readline().strip()
            year = f.readline().strip()
            position =f.readline().strip()
            if last.upper()== lastname.upper() and first.upper()== firstname.upper():
                if position == '1':
                    goldTotal= goldTotal+1
                if position == '2':
                    silverTotal= silverTotal+1
                if position == '3':
                    bronzeTotal= bronzeTotal+1
            if not f.readline():
                break
    return (goldTotal, silverTotal, bronzeTotal)


def main():
    """
        Prompts user for year to search
        Prints total gold medals won for specific year
        Prompts user for First and Last name of person
        Prints total gold, silver, and bronze medals for stated person
    """
    yearFind= input("Enter the year to count its winners: ")
    total= findGold(yearFind)
    print ("In the year",yearFind,"there were", total, "winners")
    print ("Let's look up the total medals won by an athlete (1896-2008)!")
    last= input("Last name: ")
    first= input("First name: ")
    gold,silver,bronze= medalsForPerson(first,last)
    print(first.lower().capitalize(), last.lower().capitalize(), "won ",gold, "gold,", silver, "silver,", bronze,"bronze medals.")
    
main()
    

