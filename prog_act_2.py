#Ask the user for their current age
current_age = int(input("how old are you? "))

#Ask the user what age they would like to live to
target_age = int(input("what age would you like to live to? "))

#Calculate how many years are left
Years_left = target_age - current_age

#check if the input makes sense
if Years_left <= 0:
    print("Looks like you alreadY reached (or passed) your goal age!" )
else:
    #print a friendly message
     print(f"you have about {Years_left} years left to live. Make the most of them! ")  