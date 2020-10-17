def age_calculation (age_number,days_in_a_year = 365):
    return age_number * days_in_a_year


age = input("Enter your age: ")


while int(age) <0:
    print("Error! Please enter appropriate age.")
    age = input("Enter your age: ")
    if int(age) >0:
     break

if int(age) >0:
    age_criteria = age_calculation(int(age),days_in_a_year=365)
    print(age_criteria)



