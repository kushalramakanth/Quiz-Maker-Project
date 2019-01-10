import csv
import random

def checkAns(ans,key):
    """ 
        Checks the answer for keyword
        if keyword is found
            returns 1
        else
            returns 0
            
    """
        if key in ans:
            return 1
        return 0

def main():
    print("\n----------Quiz----------\n")
    with open("questions.csv","r") as fh:
        reader = csv.reader(fh,delimiter = ",")
        data = list(reader)
        done = [] #keeps track of the question numbers to avoid repeating
        points = 0 #To track the points earned
        for i in range(5): # prints 5 random questions from the given file
            while True:
                n = random.randint(1,len(data))
                if n not in done:#checks for repetition of questions
                    done.append(n)
                    break

            print(f"\n{i+1}.{data[done[-1]][1]}")
            print("Ans:",end='')
            ans = input()# user input
            points += checkAns(ans.lower(),data[done[-1]][2])# answer given by user in lower case and the keyword is passed
        print("\n\n Total Score = ",points)
    
if __name__ == '__main__':
	main()
