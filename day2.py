#day2 assignment 

#get random names of the people in the list using for loop, maximum 
#participants variable and input() function
#and then get your lottery run

   

n=int(input("Enter number of participants ")) 

#suppose participants are 4 : = ["prabhat", "rohan", "paras", "nikin"]   

participants=[input() for i in range(n)]
print(participants)

import random                      #for generating a random number who will win 
m=random.randint(0,n-1)            #it will give you random number winner every time
print(participants[m])                    #and here we get ..the winner 
