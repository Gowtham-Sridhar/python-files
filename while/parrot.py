
prompt = 'Tell me something, I will repeat back to you.'
prompt += "\nenter 'quit' to end the program: "

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)