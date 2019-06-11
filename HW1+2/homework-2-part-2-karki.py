
#1 create list
countries = ['Indonesia','South Korea','Pakistan','Veitnam','Cambodia','Malaysia','Turkey']

#2 print list using for loop
for country in countries:
    print(country)

#3 sort permanently

countries.sort()
print(countries)

#4 display first element

print(countries[0])

#5 second to last element

print(countries[-2])

#6 deleting a value (how to do it using its name???????????????)

countries.remove("Turkey")
print(countries)

#7 capitalizing all letters

for country in countries:
    print(country.upper())

# PART TWO: Dictionaries

# 1 Create Dictionary

tree = {'name':'Jaya Sri Maha Bodhi',

'species':'Ficus Religiosa',

'age':2300,

'location_name':'Anuradhapura, Sri Lanka',

'latitude':8,

'longitude':80}

# 2 Print sentence

print(tree['name'] , 'is a', tree['age'], 'year old tree that is in' , tree['location_name'])

# 3 south of NYC?

if tree["latitude"] < 40.7128:
    print(tree['name'], "in", tree['location_name'] , "is south of NYC.")

else:
    print(tree['name'], "in", tree['location_name'] , "is north of NYC.")

age = input("How old are you?")
age = int(age)

print(tree['name'], "was", tree['age'] - int(age), "years old when you were born.")

# PART TWO

# 1

Moscow = {"name" : "Moscow", "latitude" : 55.76, "longitude" : 37.61}
Tehran = {"name" : "Tehran", "latitude" : 35.67, "longitude" : 51.37}
Falkland_Islands = {"name" : "Falkland Islands", "latitude" : -51.80, "longitude" :-58.59}
Seoul = {"name" : "Seoul", "latitude" : 37.55,  "longitude" : 126.94}
Santiago = {"name": "Santiago", "latitude" : -33.44, "longitude" :-70.67}

# 2 Above or below equator?

if Moscow["latitude"] > 0:
    print("Moscow is above equator.")

else:
    print("Moscow is below equator.")

if Tehran["latitude"] > 0:
    print("Tehran is above equator.")

else:
    print("Tehran is below equator.")

if Falkland_Islands["latitude"] > 0:
    print("Falkland Islands is above equator.")

else:
    print("Falkland Islands is below equator.")

if Seoul["latitude"] > 0:
    print("Seoul is above equator.")

else:
    print("Seoul is below equator.")

if Santiago["latitude"] > 0:
    print("Santiago is above equator.")

else:
    print("Santiago is below equator.")

# 3 North or south?

if Moscow["latitude"] > tree["latitude"]:
    print("Moscow is north of tree.")

else:
    print("Moscow is south of tree.")

if Tehran["latitude"] > tree["latitude"]:
    print("Tehran is north of tree.")

else:
    print("Tehran is south of tree.")

if Falkland_Islands["latitude"] > tree["latitude"]:
    print("Falkland Islands is north of tree.")

else:
    print("Falkland Islands is south of tree.")

if Seoul["latitude"] > tree["latitude"]:
    print("Seoul is north of tree.")

else:
    print("Seoul is south of tree.")

if Santiago["latitude"] > tree["latitude"]:
    print("Santiago is north of tree.")

else:
    print("Santiago is south of tree.")