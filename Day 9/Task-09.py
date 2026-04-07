#Keys & Values pairs
programing_dictionary = {
    "Bug": "An error in a program that prevents the programfrom running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#Printing 
print(programing_dictionary["Function"])

#Edit an item ina dictionary
programing_dictionary["Loop"]="The action of doing something over and over again."

#Looping through a dictionary
for thing in programing_dictionary:
    print(thing)

#Looping through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

#Exercise 01
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

#Nested list and dictionaries

capitals = {
    "France":"Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

travel_log = {
    "France": ["Paris","Lille","Dijon"],
    "Germany": ["stuttgart","Berlin"],
}

#print Lille
print(travel_log["France"][1])

#nested Lists
nested_list = ["A","B",["C","D"]]

#print D
print(nested_list[2][1])


travel_log = {
    "France": {
        "cities_visited":["Paris","Lille","Dijon"],
        "city_visited":8
        },
    "Germany": {
        "cities_visited": ["Berlin","Hamburg","stuttgart"],
        "total_visits": 5
    },
}


#print stuttgart
print(travel_log["Germany"]["cities_visited"][2])








#Excercise(Biding)

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is : {winner} with a bid of R{highest_bid}.")



# TODO-1: Ask the user for input
# TODO-2: save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
bids = {}
continue_biding = True

while continue_biding: #while continue_biding == True:
    name = input("What is your name?: ")
    price = int(input("What is you bid?: R"))
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_biding = False
        find_highest_bidder(bids)

    elif should_continue == "yes":
        print("\n" * 10)

        

    





