"""
Functionalities of grocery tracker:
1.Add groceries with count
2.Keep track of expiry (from loaded time to expiry time)
3.creating expiring properties of different groceries and add them accordingly
"""
import time 

# current_time_epoch=int(time.time())
# struct_time=(time.localtime(current_time_epoch))
# current_day=time.strftime("%d",struct_time)
# current_time_seconds=time.strftime("%s",struct_time)


#initialize dictionaries to store expiry and count info of groceries
groceries_expiry={}
groceries_count={}

#adds a grocery and sets expiry and count to it
def add_grocery():

    #prompt user for name,count and expiry time
    #using less seconds as expiry time for easy testing
    name=str(input("Enter a grocery name :"))
    count=int(input("Enter "+name+" count :"))
    expiry_time=int(input("In how many seconds will the "+name+" get expired? :"))

    #set current date, expiry date and count to dictionary
    groceries_expiry[name]=[int(time.time()),expiry_time]
    groceries_count[name]=[count]

#checks grocery expiry status
def check_grocery():

    #prompt user to check grocery 
    name=str(input("Enter grocery name to check:"))


    if name in groceries_expiry:
        grocery_expiry_info=groceries_expiry[name]
        exact_expiring_time=grocery_expiry_info[0]+grocery_expiry_info[1]
        while int(time.time())<exact_expiring_time:
            print("initial time: "+str(grocery_expiry_info[0]))
            print("exact expiring time: "+str(exact_expiring_time))
            print("current time: "+str(int(time.time())))
            print(name+" is not expired\n")
            time.sleep(1)
        print(name+" is expired!!!! GG's amigo, nt though")
    else:
        print("The grocery "+name+" is not available")

add_grocery()
check_grocery()
# print("Grocery count= "+str(groceries_count))
# print("Grocery expiry info= "+str(groceries_expiry))

