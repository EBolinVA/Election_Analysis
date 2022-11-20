# set up a list of dictionaries of voting data
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# print each dictionary in the list, using standard format for iterating over the list of dictionaries with a for loop
# for county_dict in voting_data:
#    print(county_dict)

# only print the county using the range() function to iterate over the list of dictionaries
# remember that 'county' is defined within the dictionaries
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# to get only the values from each dictionary in the list of dictionaries,
# we need to use a nested for loop. 
# First, use the for loop to retrieve each dictionary
# for county_dict in voting_data:

# Second, use the values() method on the variable county_dict to reference the data in the second for 
#loop in order to get each value
    # for value in county_dict.values():
        # print(value)