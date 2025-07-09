#Peter Mantilla

def ageChecker_dis(age): #takes age as in input and sees if user can get a discount
    po = 0.00
    if (age >= 65):
        po = po+0.10
    elif (age <= 12):
        po = po+0.10
    return po

def ageChecker_A(total, age,booze,booze_c): # takes severall inputs to see if user is old enough
    if (age < 21 and booze ==True):
         total = total - (5.00*booze_c)
         print("Item removed from cart")
    return total





def main(): #main function the simulates a shopping enviroment 
    print("Welcome to shoping")
    while True: #main loop that runs the function
        
#----------------------------------    varible defined    
        po = 0.00
        total = 0.00
        booze = False
        add = ""
        age = 0
        member = "n"
        booze_c = 0
#----------------------------------       
        try: # a try loop to prevent crashes
           
            while True: # takes user input and calculates base cost
                cart = int(input("type 1 for Apple, Type 2 for booze, 3 pasta, 4 dough "))
                if(cart==1):
                    total = total+3
                if(cart==2):
                    total = total+5
                    booze = True
                    booze_c = booze_c + 1
                if(cart==3):
                    total = total+4
                if(cart==4):
                    total = total+3.5    
                print("Current cost $"+ format(total))
                add = str(input("continue? enter y for yes or n for No"))
                if (add== "n"):
                   # print("break works") <-used to be a check to see if it was woring no longer used 
                    break
            
            #print("yippee") <-used to be a check to see if it was woring no longer used 
            member = str(input("are you a member? y for yes, n for no"))
            age = int(input("What is your age in years"))
           
            po=po + ageChecker_dis(age) #checks for discounts based on age
            total = ageChecker_A(total,age,booze,booze_c) #sees if the user is able to buy booze
 
            if (member == "y"): #sees if user is a member and wether or not to apply a discount
                po = po + 0.10
            buy = str(input("your total is $"+format(total*(1.00-po),'.2f')+" would you like to purchase, y for yes, n for no"))
            if (buy == "y"):
                print("purchase compleate, thank you for shoping")
        finally: #leaves the try statment
            again = input("shop again, y for yes, n for no")
            if (again!="y"):
                break

main()