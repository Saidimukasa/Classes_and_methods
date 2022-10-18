def person():
    name = input("Enter the name : ") #allows a user to enter the name
    weight = float(input("Enter the weight : "))
    birth_date = 2002 # taking all users to have the same birthdate
    age = 2022-birth_date 
    if name == "": # if no name has been entered
        print("\n name : name" ,"\n weight : ",weight, "\n birthdate : ",birth_date)
        print("age" , age)
    else:
        print("\n name : ",name ,"\n weight : ",weight, "\n birthdate : ",birth_date)

def main():
    person()
main()
