import re

def normalize_phone(phone_number):
    formatted_phone = re.sub(r'[^0-9+]', '', phone_number)
    if formatted_phone[0:2] == '38':
        return '+' + formatted_phone
    elif formatted_phone[0] == '0':
        return '+38' + formatted_phone
    else:
        return formatted_phone
