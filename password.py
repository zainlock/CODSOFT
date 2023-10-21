import random
latter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']
special_character=['@','#','!','$','%','^','&','*','(',')']

#take input from user
size_of_Character=int(input("Enter a number of character you want: "))
size_of_number=int(input("Enter a numbers of number you want: "))
size_of_special=int(input("Enter a number of special character do you want: "))

password=""
strong_password=""

for char in range(1,size_of_Character+1):
    password+=random.choice(latter)
    
for num in range(1,size_of_number+1):
    password+=random.choice(number)
    
for sep in range(1,size_of_special+1):
    password+=random.choice(special_character)
    
for strong in range(1,len(password)):
    strong_password+=random.choice(password)
    
print('The password is :',password)
print("The Strong password is:",strong_password)

