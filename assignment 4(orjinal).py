#Getting an input from the user.
birth_date_str= input("Enter your birthday:")
#Turning the input to integer.
birth_date =int(birth_date_str)
if 1883 <= birth_date <= 1900:
    print("You are Lost Generation!")
elif 1901 <= birth_date  <= 1927:
    print("You are Greatest Generation!")
elif 1928 <= birth_date  <= 1945:
    print("You are Silent Generation!")
elif 1946 <= birth_date  <= 1964:
    print("You are Baby Boomers!")
elif 1965 <= birth_date  <= 1980:
    print("You are Generation X!")
elif 1981 <= birth_date  <= 1996:
    print("You are Milennials!")
elif 1997 <= birth_date  <= 2012:
    print("You are Generation Z!")
elif 2012 < birth_date:
    print("You are Generation Alfa!")
#If the variable birth_date is too small,program may get an error.
#This part is to prevent it from happening.
else:
    print("Dude,you shouldn't be alive!")