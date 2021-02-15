str ="I'm writing some test string and you should finde something in it"
substr = str.find("some", 20, 50)
print(substr)



'''
sum = 0
count = 0
max = 0
min = 0
while True:
    number = input("Enter a number (Enter 'done' to exit): ")
    if number == 'done':
        break
    try:
        number = int(number)
        count += 1
        sum += number
        if number > max:
            max = number
        if number < min:
            min = number
    except:
        print("You should only enter integer numbers!")
print ("You entered ", count , "numbers")
print ("Sum is: ", sum)
print ("Max is: ", max)
print ("Min is: ", min)
if count > 0:
    print ("Average is: ", sum/count)
'''


'''
from tkinter import Tk, Label, Frame, Entry, Button, Spinbox
 
def press():
    usr = u.get()
    psw = p.get()
    if usr == "Poulstar" and psw == "12345":
        print("LOGGED IN!")
    else:
        print("No, no, no!")
        
root = Tk()

age = Tk.Spinbox(root, from_=0, to=100)
age.pack()

user = Frame(root)
user.pack(side='top')
Label(user, text="Username").pack(side='right')
u = Entry(user)
u.pack(side='left')
 
password = Frame(root)
password.pack(side='top')
Label(password, text="Password").pack(side='left')
p = Entry(password, show="*")
p.pack(side='left')
 
buttons = Frame(root)
buttons.pack(side='bottom')
Button(buttons, text="Login", command=press).pack(side='left')
Button(buttons, text="Cancel", command=root.destroy).pack(side='left')
 
root.mainloop()
'''

 
'''
File = open('numbers.txt', 'r')
mystr = File.readlines()
for i in range (mystr.__len__()):
    print(mystr[i])
File.close()
'''

'''
from tkinter import Tk, Frame, Button, Grid, Label, StringVar
from time import sleep
import datetime
 
def two_digit(value):
    if value < 10:
        return "0"+str(value)
    else:
        return str(value)
 
def convert_to_time(time):
    hour = int(time/3600)
    minute = int(time/60) - hour*60
    second = time - (hour*3600) - (minute*60)
    time_str = two_digit(hour)+":"+two_digit(minute)+":"+two_digit(second)
    return time_str

def update_times():
    global p1Time, p2Time, p1TimeStr, p2TimeStr,p1t,p2t
    p1t=convert_to_time(p1Time)
    p2t=convert_to_time(p2Time)
    p1TimeStr.set(p1t)
    p2TimeStr.set(p2t)
 
def updater_loop():
    global app, p1Time, p2Time, p1Active, p2Active
    while True:
        update_times()
        app.update()
        sleep(0.01)
        if p1Active:
            p1Time += 1
 
        if p2Active:
            p2Time += 1
 
def p1_clicked():
    global p1Active, p2Active
    p1Active = not p1Active
    if p1Active:
        state="player 1 : "
    else:
        state="player 1 stop : "
 
    f=open("time.txt","a")
    t=datetime.datetime.now().strftime("%H:%M:%S")
    f.write(state+" started at "+str(t)+"------"+"time:"+p1t+"\n")
    f.close()
    p2Active = False
 
def p2_clicked():
    global p1Active, p2Active
    p1Active = False
    p2Active = not p2Active
    if p2Active:
        state="player 2 : "
    else:
        state="player 2 stop : "
 
    f = open("time.txt", "a")
    t = datetime.datetime.now().strftime("%H:%M:%S")
    f.write(state+" started at "+str(t)+"------"+"time:"+p2t+"\n")
    f.close()
 
app = Tk()
app.resizable(1, 1)
app.geometry('200x250')
p1Active = False
p2Active = False
p1Time = 0
p2Time = 0
p1TimeStr = StringVar()
p2TimeStr = StringVar()
update_times()
 
lblTimeP1 = Label(app, text="Player 1")
lblTimeP1.pack(side="top", fill="x")
lblTimeP1 = Label(app, text="Player 2")
lblTimeP1.pack(side="bottom", fill="x")
 
lblTimeP1 = Label(app, textvariable=p1TimeStr)
lblTimeP1.pack(side="top", fill="x")
lblTimeP2 = Label(app, textvariable=p2TimeStr)
lblTimeP2.pack(side="bottom", fill="x")
 
btnFrame = Frame(app, bg="#00ff00")
btnFrame.pack(expand=True, fill="both")
 
btnPlayer1 = Button(btnFrame, text="Player 1", bg="#ff0000", foreground="#ffffff", command=p1_clicked,height=5)
btnPlayer1.pack(side="top", fill="both")
 
btnPlayer2 = Button(btnFrame, text="Player 2", bg="#0000ff", command=p2_clicked,height=5)
btnPlayer2.pack(side="bottom", fill="both")
updater_loop()
'''


'''
import tkinter
 
def check():
    global temp
    if temp<30:
        Label2['background'] = 'green'
        Label2['text'] = 'Off'
    if temp>=30:
        Label2['background'] = 'red'
        Label2['text'] = 'On'
 
def up():
    global temp
    temp += 1
    Label1['text']=temp
    check()
    
def down():
    global temp
    temp -= 1
    if temp<0:
        temp = 0
    Label1['text']=temp
    check()
temp = 0
 
root = tkinter.Tk()
root.title("Mindow")
root.geometry("300x500")
 
u = tkinter.Button(root, text="up", command=up)
u.pack()
 
Label1 = tkinter.Label(root, text=temp)
Label1.pack()

d = tkinter.Button(root, text="down", command=down)
d.pack(fill = 'both', expand = 0)
 
Label2 = tkinter.Label(root, text="Off")
Label2.pack()
 
check()
root.mainloop()
'''


'''
def login (user, password):
    if (user == "poul" and password == "poul"):
        return True
    else:
        if (user != 'poul'):
            print("Enter correct user:")
        else:
            print("Enter correct pass:")
        return False

for x in range (0, 3):
    user = input("Enter Username:")
    password = input("Enter Password:")
    result = login(user, password)
    if(result == True):
        print("Yey")
'''

'''
import turtle
t=turtle.Pen()
t.pencolor("red")
def square(step):
    a=[1,2,3,4]
    for i in a:
        t.forward(step)
        t.left(90)
def move(step):
    t.penup()
    t.left(90)
    t.forward(step)
    t.right(90)
    t.forward(step)
    t.pendown()
square(100)
move(25)
square(50)
move(12)
square(25)
move(6)
square(13)
move(3)
square(6)
turtle.done()
'''


'''
import turtle
t=turtle.Pen()
for i in range (100):
    t.forward(i)
    t.left(90)
turtle.done()
'''

'''
import turtle
test = turtle.Turtle()
test.shape("turtle")
for i in range (1, 10):
    test.circle(i*10)
turtle.done()
'''

'''
import turtle
t = turtle.Pen()
t.pencolor("cyan")
t.left(70)
t.forward(100)
t.right(70)
t.forward(200)
t.right(110)
t.forward(100)
t.right(70)
t.forward(200)
t.right(135)
t.penup()
t.forward(30)
t.pendown()
t.pencolor("red")
t.left(25)
t.forward(60)
t.right(70)
t.forward(150)
t.right(110)
t.forward(60)
t.right(70)
t.forward(150)
turtle.done()
'''

'''
dama = input("Enter dama:")
dama = int(dama)
if dama>30:
    print("It's hot.")
elif dama >20:
    print("It's warm.")
elif dama >10:
    print("It's good.")
elif dama >0:
    print("It's cold.")
else:
    print("It's very cold.")
'''

'''
import turtle
r = input("Enter radius:")
f = input("Enter forward:")
b = input("Enter backward:")
r = int(r)
f = int(f)
b = int(b)
test = turtle.Turtle()
test.shape("turtle")
test.forward(f)
test.circle(r)
test.backward(b)
turtle.done()
'''