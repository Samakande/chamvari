import random, time
def fill(field, text):
    for char in text:
        time.sleep(random.uniform(0.178742, 0.85547))
        field.send_keys(char)
