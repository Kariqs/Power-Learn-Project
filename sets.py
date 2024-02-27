companies = {"Apple","Microsoft"}
food_companies = {"Zesta","Pwani"} 
print(companies)
companies.add("Karitech")#add value to a set.
companies.discard("Apple")#remove value to a set
print(companies)
# companies = companies|food_companies
print("The united set is:",companies.union(food_companies)) #union of a set.
