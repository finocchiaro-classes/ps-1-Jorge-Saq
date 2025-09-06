#Creating variable for recidivism risk
risk = 0

#Ask for Prior arrest
prior_arrest = int(input("Prior arrests: "))

#Ask if arrest were local ordinance
local_ordinance = input("Prior arrests for local ordinance (Y/N): ")

#Ask for age of release
age_of_release = int(input("Age at release: "))

#Adds points based on prior arrest
if(prior_arrest >=5):
    risk+=2
elif(prior_arrest >=2):
    risk+=1

#Adds points if prior arrest was for local ordinance
if(local_ordinance == "Y"):
    risk+=1
    
#Adds/subtracts points based on age of release
if(age_of_release>=18 and age_of_release<=24):
    risk+=1
elif(age_of_release>=40):
    risk-=1
    
#print recidivism risk score
print(f"The recidivism risk score is {risk}")
