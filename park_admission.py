# Park admission DisneyVerse

print("\t\tWelcome to DisneyVerse")
user_name = input("\t\tPlease enter your name: \n")

print('\t\tPlease, choose the right package for you:\n "Hello DisneyVerse" - 1 Day Admission\n '
      '"Happy DisneyVerse" - 2 Days and 1 Night Admission\n "I Love DisneyVerse" - 5 Days and 4 Nights Admission ')

answer = input()

h_d = "Hello DisneyVerse"
ha_d = "Happy DisneyVerse"
i_l_d = "I Love DisneyVerse"

age = int(input("\t\tPlease enter your age: \n"))
if age <= 5:
    price_age = 0
elif age < 12:
    price_age = 25
else:
    price_age = 40

if h_d == answer:
    price = 120
elif ha_d == answer:
    price = 250
elif i_l_d == answer:
    price = 800
else:
    price = None
    print("The error occurred, please try again")

print(f"Congratulations! Thank you for choosing US! Your admission cost is ${price + price_age}.")




