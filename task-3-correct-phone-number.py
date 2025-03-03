import re

def normalize_phone(phone_number):
    correct_phone_number = ""
    if re.search(r"380", phone_number):
        correct_phone_number = '+'
        correct_phone_number += str((re.sub(r"(\D)", '', phone_number)))
   
    else:
        correct_phone_number = '+38'
        correct_phone_number += str((re.sub(r"(\D)", '', phone_number)))

    return correct_phone_number
            
