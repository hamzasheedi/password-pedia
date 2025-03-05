import random
import string
import streamlit as st

#-------------------------
# PASSWORD GENERATOR FUNCTION 
#-------------------------

def generate_password(length=12):

    #-------------------------
    # Ensuring at least one of each type
    #-------------------------
    
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()-_=+{}[]|;:'\",.<>?/`~")
    
    #-------------------------
    # Fill remaining with random choices
    #-------------------------
    
    remaining_chars = ''.join(random.choices(
        string.ascii_letters + string.digits + "!@#$%^&*()-_=+{}[]|;:'\",.<>?/`~", k=length-3))
    
    password_list = list(uppercase + digit + special + remaining_chars)
    random.shuffle(password_list)
    
    return ''.join(password_list)



