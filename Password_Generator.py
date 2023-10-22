 import string
import random
def cal():
    character_lower=string.ascii_lowercase
    character_upper=string.ascii_uppercase
    Digits=string.digits
    special_character=string.punctuation
    store=[] 
    store.extend(list(character_lower))
    store.extend(list(character_upper))
    store.extend(list(Digits))
    store.extend(list(special_character))
    random.shuffle(store)
    password="".join(store[0:user_len])
    print("Your password is:",password)
    
try:
    user_len=int(input("Enter Password Length: \n"))
    if(user_len!=str):
            cal()
except ValueError:
    print("Please enter a valid number")
