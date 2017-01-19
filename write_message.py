filename = "reasons.txt"

prompt = "Why are you fond of programming?\n"
prompt += "'quit' to end it\n "

is_going_on = True

while is_going_on:
    reason = input(prompt)
    if reason == 'quit':
        is_going_on = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(reason + '\n')