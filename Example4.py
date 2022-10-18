def person(name,birth_year ,weight):
    age = 2022-birth_year
    if name == "": # if no name has been entered
        print("\n name : name" ,"\n weight : ",weight, "\n birthdate : ",birth_year)
        print("\n age" , age)
    else:
        print("\n name : ",name ,"\n weight : ",weight, "\n birthdate : ",birth_year,"\n age" , age)

def main():
    name = input("Enter the name : ") #allows a user to enter the name
    weight = float(input("Enter the weight : "))
    birth_year = 2002 # taking all users to have the same birthdate
    person(name,birth_year ,weight) # void function
main()
