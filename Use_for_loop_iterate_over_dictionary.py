counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#get only the keys from a dictionary using a for loop
for county in counties_dict:
    print(county)

#use the keys() method (it doesn't matter what variable name we use in the for loop)
for county in counties_dict.keys():
    print(county)

# to get the values of a dictionary, use the .values() method
for voters in counties_dict.values():
    print(voters)

# you can also use the format dictionary_name[key] to get the value for the key
for county in counties_dict:
    print(counties_dict[county])

# another way to get values of a key is to use the get() method on the dictionary in the for loop
for county in counties_dict:
    print(counties_dict.get(county))

# to print the key-value pair of the dictionary, we use the items() method in the for loop
for key, value in counties_dict.items():
    print(key, value)

#can be referenced by "county" and "voter" or key, value as above
for county, voters in counties_dict.items():
    print(county, voters)

# skill drill print county and voter in sentence format
for county, voter in counties_dict.items():
    print(county + " county has " + str(voter) + " registered voters.")

# rewrite code above using f-string
for county, voter in counties_dict.items():
    print(f"{county} county has {voter:,} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
