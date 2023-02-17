#light_theme{
# "button:"red",
# "title":"blue"}
# dark_theme= {
#     "button":"black",
# "title":"white"}
# example
# pawn={"direction":["right","left"],
#       "level:least"}
# king={"direction":"all",
#       "level":"highest"}
# def average(a,b):
#     av=(a +b)/2 
#     return av
# print(av)

#scope
#1. local scope a local varibale that is inside a function can only be used inside the function
# 2. global scope  can  be used 

# m=30
# y=40
# def check(a):
#     x=a*5
#     x=m+y
#     return x
# global variable=m,y
#local variable = x
# cars={
#     "model":"ford",
#     "year":1998,
#     "colour":"red",
#     "country":"kenya"
#}
# print(cars["year"])
# #accessing dictionaries items
# print(cars["country"])
# person ={
#     "name":"esborn",
#     "country":"kenya",
#     "pet":["dog","cat"]
    
# }
# print(person["name"])
# print(person["pet"][1])

# person ={
#     "name":"cathy",
#     "age":23,
#     "pets":{"dog":"x",
#            "cats":"y"}
# }
# print(person["pets][0]
# teams={
#     23:"a",
#     56.67:"b",
#     names:{blue":"m",
#     "yellow":"n"
#     }
#     print(teams[blue])


# }

# profile ={}
# profile["username"]="user123"
# profile["age"]=20
# profile["email"]="esbornchiira8@gmail.com"
# profile["age"]:20
# print(profile)
profile={}
def register():
    #ask for name then password then email then store in a dictionary
    username=input("Enter username:")
    email=input("Enter email:")
    password=input("Enter password:")
    #store in a dictionary
    profile["username"]= username
    profile["email"]= email
    profile["password"]= password
def get_profile():
    #print the user profile 
    print(profile)    
def change_username():
    new_name=input("Enter new username:")   
    profile["username"]=new_name
register()
get_profile()
change_username()
get_profile()


