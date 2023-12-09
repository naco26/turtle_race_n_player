import turtle as t
import random

#variable declaration
color = ["violet","indigo","blue","green","yellow","orange","red"] #7 diff colors of turtle players
is_race_on=False # determine length of the race 
turtles = []
sc = t.Screen()
x=500 # x cor of screen
y=400 # y cor of screen
sc.setup(width=x,height=y)

#turtle which show game over text
t1 = t.Turtle(shape="turtle")
t1.hideturtle()

##Taking user bet - any num of players can play this
chosen_turtles=[]
players_names=[]
players = sc.numinput(title="VIBGYOR Turtle Race",prompt="How many are you? Enter num:")
for i in range(0,int(players)):
    player_name=sc.textinput(title="VIBGYOR Turtle Race",prompt="Enter your name:")
    if player_name!='':
        players_names.append(player_name)
    chosen_turtle=sc.textinput(title="VIBGYOR Turtle Race",prompt="Which turtle player do you want to bet on? Enter a color:")
    if chosen_turtle!='':
        chosen_turtles.append(chosen_turtle)

##Our 7 turles players are getting ready
for i in range(0,7):
    tim1 = t.Turtle(shape="turtle")
    tim1.color(color[i])
    turtles.append(tim1)


##moving turtles to starting position.
j=-(y/2)
for t in turtles:
    t.penup()
    t.goto(-((x/2)-30),j+50)
    j+=50

## making sure bet is made
if len(chosen_turtles)==int(players) and len(players_names)==int(players):
    is_race_on=True
else:
    t1.write("Invalid inputs!!",align="center",font=('Arial', 30, 'normal'))

##Starting race
while is_race_on:
    for t in turtles:
        t.forward(random.randint(0,10))
        t.speed(random.randint(0,4))
        
        #checking if winner can be decided and exiting
        if t.xcor()>((x/2)-20):
            is_race_on=False
            writetext = "Game Over!!!"
            win_turtle=t.pencolor()
            print(f"Winning turle is {win_turtle}")
            winers=[]
            for i in range(0,int(players)):
                if win_turtle==chosen_turtles[i]:
                    print(f"{players_names[i]} win.")
                    winers.append(players_names[i])
                    t.write(win_turtle)
                else:
                    print(f"{players_names[i]} loose.")
            if len(winers)>0:
                writetext+= ",".join(winers)+" won :)"
            if "won" not in writetext:
                writetext+="You loose :("
            #Display Game over and winning text
            t1.write(writetext,align="center",font=('Arial', 30, 'normal'))


#exit
sc.exitonclick()