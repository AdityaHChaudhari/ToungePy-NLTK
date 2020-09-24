import sys
dictr = {
    #users information
    "name" : " ",
    "Date" : " ",
    "actor" : " ",
    "color" : " ",
    "singer" : " ",
    }
greet = "Hi "
i = 0
def compare(string1,string2):
    if string1==string2:
        return 0
        
def speak(string):
    print("Techno : "+string)
    
def compare(op,string):
    return (op == string)
    
def assign(op1,op3):
    dictr[op1] = op3
    speak("I will remember it.")
    
def listen():
    ip = input(User+" : ")
    ip = [ip]
    return ip
    
def convert(lst):
    return lst[0].split()

def lexer():
    i_p = listen()
    op = convert(i_p)
    if op[0]=="My":
        if op[1] == "name":
            if op[2] == "is":
                assign(op[1],op[3])
        if op[1] == "favourite":
            if op[2] == "actor":
                if op[3] == "is":
                    assign(op[2],op[4])
            elif op[2] == "color":
                if op[3] == "is":
                    assign(op[2],op[4])
            elif op[2] == "singer":
                if op[3] == "is":
                    assign(op[2],op[4])
    elif op[i] == "What":
        if op[i+1] == "is":
            if op[i+2] == "my":
                if op[i+3] == "name?":
                    speak(dictr["name"])
            if op[i+2] == "your":
                if op[i+3] == "name?":
                    speak("My name is Techno")
                    
    elif op[i] == "Which":
        if op[i+1] == "is":
            if op[i+2] == "my":
                if op[i+3] == "favourite":
                    if op[i+4] == "color?":
                        speak(dictr["color"])
    elif op[i] == "Who":
        if op[i+1] == "is":
            if op[i+2] == "my":
                if op[i+3] == "favourite":
                    if op[i+4] == "actor?":
                        speak(dictr["actor"])
                    elif op[i+4] == "singer?":
                        speak(dictr["singer"])
        if op[i+1] == "are":
                if op[i+2] == "you?":
                    speak("I am your persnol assistant")                      
    else:
        speak("Incorrect Sentance !")
        speak("Please write again")
    return lexer()
            
speak("What is your name ?")
dictr["name"] = input("->")
User = dictr["name"]
speak(greet+User)
speak("What can I do for you ?")
lexer()
