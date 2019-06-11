print("ARUN KARKI")
print("May 28, 2019")
print("Homework 1")


#1. Prompt the user for their year of birth, and tell them (approximately):

print("What year were you born?")
(year_of_birth)= input()

current_year=2019

if int(year_of_birth) < current_year:
    print("Please confirm your birth year again.")
    (real_year_of_birth)= input()
    age=current_year-int(real_year_of_birth)
    print("You're", age , "years old.")
    
elif int(year_of_birth) > current_year:
    print("Time Machines only exist in Hollywood movies.") 
    print("Your real birth year?")
    (real_year_of_birth)= input()
    age=current_year-int(real_year_of_birth)
    print("You're", age , "years old.")
    
    
#  3. How many times the user's heart has beaten?
bpm=70
Heartbeat=bpm*60*24*365*age
print("Your heart has beaten ", int(Heartbeat), " times.")


# 4. How many times a blue whale's heart has beaten?
# https://www.whalefacts.org/blue-whale-heart/

Blue_Whale_Heart_Beat=9*60*24*365*age
print("A blue whales' heart has beaten ", Blue_Whale_Heart_Beat, "times.")

# 5. How many times a rabbit's heart has beaten?
# https://rabbit.org/temperature-and-respiration-rates/

Rabbit_Heart_Beat=135*60*24*365*age
print("A rabbit's heart has beaten", int(Rabbit_Heart_Beat/1000000), " million times.")

# 7. How old they are in Venus years?
Venus_days = 225
print("You are ", Venus_days/age, "Venus years old.")

# 8. How old they are in Neptune years?
one_neptune_yr = 165
one_earth_yr = 1/one_neptune_yr
neptune_age_user = one_earth_yr*age
print("You are ", neptune_age_user, "Neptune years old.")

# 9. Whether they are the same age as you, older or younger?
my_age = 35
if age > my_age:
    print("You're older than me.")
elif age < my_age:
    print("You're younger than me.")
else:
    print("Our age is same.")

# 11. If they were born in an even or odd year?
if age/2 == 0:
    print("Even")
else:
    print("Odd")


# # 1. How many accidents are in the file?
# date_last = 2/11/2017
# date_first = 0/24/2016
# no_of_accidents = date_last-date_first
# print("There are", no_of_accidents, "in the file.")

# 12. Which US President was in office when they were born (1935 onward)

pres = "was president when you were born."

if int(real_year_of_birth) >= 2017:
    print("Trump", pres)

elif int(real_year_of_birth) >= 2009:
    print("Obama", pres)

elif int(real_year_of_birth) >= 2001:
    print("Bush", pres)

elif int(real_year_of_birth) >= 1993:
    print("Clinton", pres)

elif int(real_year_of_birth) >= 1989:
    print("H.W Bush", pres)

elif int(real_year_of_birth) >= 1981:
    print("Reagan", pres)

elif int(real_year_of_birth) >= 1977:
    print("Carter", pres)

elif int(real_year_of_birth) >= 1974:
    print("Ford", pres)

elif int(real_year_of_birth) >=1969:
    print("Nixon", pres)

elif int(real_year_of_birth) >=1961:
    print ("Kennedy", pres)

elif int(real_year_of_birth) >= 1953:
    print("Eisenhower", pres)

elif int(real_year_of_birth) >= 1945:
    print("Truman", pres)

elif int(real_year_of_birth) >= 1933:
    print("Roosevelt", pres)

elif int(real_year_of_birth) >= 1929:
    print("Hoover", pres)

elif int(real_year_of_birth) >= 1923:
    print("Coolidge", pres)

elif int(real_year_of_birth) >= 1921:
    print("Harding", pres)

elif int(real_year_of_birth) >= 1913:
    print("Wilson", pres)









