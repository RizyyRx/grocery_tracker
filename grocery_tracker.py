"""
Functionalities of grocery tracker:
1.Add groceries with count
2.Keep track of expiry (from loaded time to expiry time)
3.creating expiring properties of different groceries and add them accordingly
"""
import time 

# current_time=time.time()
# print(current_time)

# struct_time=(time.localtime(current_time))
# print(struct_time)

# formatted_time=time.strftime("%d",struct_time)
# print(formatted_time)

#initialize dictionaries to store expiry and count info of groceries
groceries_expiry={}
groceries_count={}

#adds a grocery and sets expiry and count to it
def add_grocery():

    #prompt user for name,count and expiry time
    name=str(input("Enter a grocery name :"))
    count=int(input("Enter "+name+" count :"))
    expiry_time=int(input("In how many days will the "+name+" get expired? :"))

    #set the data to dict
    groceries_expiry[name]=[expiry_time]
    groceries_count[name]=[count]

add_grocery()
print("Grocery count= "+str(groceries_count))
print("Grocery expiry info= "+str(groceries_expiry))

