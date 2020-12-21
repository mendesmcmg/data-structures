# In 2020, Santa Claus will not be able to leave the house to deliver gifts due to the Coronavirus pandemic. So he ordered his gnomes to deliver on Christmas Day. As they are quite inexperienced, they will split into several teams made up of three members: a leader, a delivery man and a sled driver. Santa's plan is for team leaders to always be the oldest gnomes, so he asked everyone to write their names and ages on a list. As you are a programmer gnome, you decided to help Santa Claus organize the list and assemble the teams from it.

# Here are some rules:
# - The list must be organized in descending order of age;
# - If two gnomes are the same age, they must be organized in ascending order of name;
# - There are no two gnomes of the same name;
# - No gnome has more than 20 characters in his name;
# - The gnomes on the list are between 10 and 100 years old;
# - The first 1/3 of the gnomes (the oldest), will be the team leaders;
# - The order of the delivery gnomes and pilots follows the same logic as the leaders. Ex) If there are 6 gnomes on the list, there will be two teams, where the oldest gnome is the leader of team 1, and the second oldest is the leader of team 2. The third oldest is the delivery man for team 1 and the fourth oldest delivery man for team 2. The fifth is a sled driver for team 1 and the last is a driver for team 2;

# Input
# The input is made up of an integer N (3 <= N <= 30), where N is a multiple of 3, which represents the number of gnomes in the list. Then the next N lines contain the name and age of each gnome.

# Output
# The output is composed of 4 lines per team. The first line must follow the format "Time X" (in English, Team X), where X is the team number. The second, third and fourth lines contain, respectively, the name and age of the leading gnome, delivery man and sled driver. After each team, there should be a blank line, even after the last team.

# Input Sample
# 6
# Josh 56
# Alfred 32
# Joshua 34
# Harley 61
# Peggy 60
# Jim 25

# Output
# Time 1
# Harley 61
# Josh 56
# Alfred 32
# Time 2
# Peggy 60
# Joshua 34
# Jim 25

# Input
# 9
# Kepeumo 67
# Necoi 62
# Seies 77
# Ciule 49
# Gyun 99
# Finron 27
# Norandir 66
# Galvaindir 55
# Pinhuobor 70

#Output
# Time 1
# Gyun 99
# Kepeumo 67
# Galvaindir 55
# Time 2
# Seies 77
# Norandir 66
# Ciule 49
# Time 3
# Pinhuobor 70
# Necoi 62
# Finron 27

number = int(input())
total = {}
ordertotal = {}
teams = {}
teamn = int(number/3)
key_list = []

for i in range(number):
    i, total[i] = input().split()
    total[i] = int(total[i])

#Ordenar
ordered = sorted(total, key=total.get, reverse=True)

for v in ordered:
    ordertotal[v] = total[v]

for key in ordertotal:
    key_list.append(key)

for i in range(teamn):
    teams[i+1] = {}
    teams[i+1][key_list[i]] = ordertotal[key_list[i]]

counter = 0
for d in range(teamn, 2*teamn):
    counter +=1
    teams[counter][key_list[d]] = ordertotal[key_list[d]]

counter = 0
for sd in range(2*teamn, 3*teamn):
    counter +=1
    teams[counter][key_list[sd]] = ordertotal[key_list[sd]]

for key in teams:
    if key != 1:
        print()
    print(f"Time {key}")
    for i in teams[key]:
        print(i, teams[key][i])
