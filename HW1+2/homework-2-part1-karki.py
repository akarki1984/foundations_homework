
#Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0 ,-10, 3, 22 ,48]

#Display the number of elements in the list.
print(len(numbers))

#Display the 4th element of this list.
print(numbers[3])

#Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])

#Display the last element of the original unsorted list

print(numbers[-1])

#7 Display the sum of all of the numbers divided by two.

print(sum(numbers)/2)

#8 mean or mdn greater?
import statistics
median = statistics.median(numbers)

print(median)
mid = (len(numbers) /2)
mid = int(mid)

mdn = numbers[mid] #numbers[3]

print("median is" ,mdn)

mean = sum(numbers)/len(numbers)

if mdn > mean:
    print("Median is greater.")

else:
    print("Mean is greater.")

# Part one - Dictionaries

#1 creating a dictionary about movies and printing output

movie = {"title" : "Lord of The Rings", "year" : "2001", "director" : "Peter Jackson"}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

#2 adding keys budget and revenue and printing difference

movie['budget'] = 9300000
movie['revenue'] = 871500000

print("It made a profit of $" , movie['revenue'] - movie['budget'])

#3 what kind of investment was it?

if movie['revenue'] > movie['budget']:
    print("It was a great investment!")

elif movie['budget'] > movie['revenue']:
    print("It was a bad investment.")

else:
    print("It was an okay investment.")

#4 Dictionary population NYC boroughs

pop = {"Manhattan" : 1.6,
"Brooklyn" : 2.6, 

"Bronx": 1.4, 

"Queens" : 2.3, 

"Staten Island" : 0.47 }


#5
print("Brooklyn has a population of" , pop["Brooklyn"], "million.")

#6

print("The total population of the boroughs is" , sum(pop.values()), "million.")

#7 % of Manht pop in nyc

print((pop["Manhattan"] / sum(pop.values())) * 100 , "percent of people in NYC live in Manhattan.")