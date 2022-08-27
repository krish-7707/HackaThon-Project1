import random
import array
import time
import turtle
MAX_LEN = 10
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

SYMBOLS = ['@', '#', '$', '%', '.','*']
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
        password = password + x

def snake_game():
        delay = 0.1
        score = 0
        high_score = 0

        wn = turtle.Screen()
        wn.title("Snake Game")
        wn.bgcolor("blue")

        wn.setup(width=600, height=600)
        wn.tracer(0)

        head = turtle.Turtle()
        head.shape("circle")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "Stop"

        food = turtle.Turtle()
        colors = random.choice(['red', 'green', 'black'])
        shapes = random.choice(['square', 'triangle', 'circle'])
        food.speed(0)
        food.shape(shapes)
        food.color(colors)
        food.penup()
        food.goto(0, 100)

        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score : 0 High Score : 0", align="center",
                        font=("candara", 24, "bold"))
        def group():
                if head.direction != "down":
                        head.direction = "up"


        def godown():
                if head.direction != "up":
                        head.direction = "down"


        def goleft():
                if head.direction != "right":
                        head.direction = "left"


        def goright():
                if head.direction != "left":
                        head.direction = "right"


        def move():
                if head.direction == "up":
                        y = head.ycor()
                        head.sety(y+20)
                if head.direction == "down":
                        y = head.ycor()
                        head.sety(y-20)
                if head.direction == "left":
                        x = head.xcor()
                        head.setx(x-20)
                if head.direction == "right":
                        x = head.xcor()
                        head.setx(x+20)

        wn.listen()
        wn.onkeypress(group, "w")
        wn.onkeypress(godown, "s")
        wn.onkeypress(goleft, "a")
        wn.onkeypress(goright, "d")
        segments = []

        while True:
                wn.update()
                if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                        time.sleep(1)
                        head.goto(0, 0)
                        head.direction = "Stop"
                        colors = random.choice(['red', 'blue', 'green'])
                        shapes = random.choice(['square', 'circle'])
                        for segment in segments:
                                segment.goto(1000, 1000)
                        segments.clear()
                        score = 0
                        delay = 0.1
                        pen.clear()
                        pen.write("Score : {} High Score : {} ".format(
                                score, high_score), align="center", font=("candara", 24, "bold"))
                if head.distance(food) < 20:
                        x = random.randint(-270, 270)
                        y = random.randint(-270, 270)
                        food.goto(x, y)
                        new_segment = turtle.Turtle()
                        new_segment.speed(0)
                        new_segment.shape("square")
                        new_segment.color("orange")
                        new_segment.penup()
                        segments.append(new_segment)
                        delay -= 0.001
                        score += 10
                        if score > high_score:
                                high_score = score
                        pen.clear()
                        pen.write("Score : {} High Score : {} ".format(
                                score, high_score), align="center", font=("candara", 24, "bold"))
                for index in range(len(segments)-1, 0, -1):
                        x = segments[index-1].xcor()
                        y = segments[index-1].ycor()
                        segments[index].goto(x, y)
                if len(segments) > 0:
                        x = head.xcor()
                        y = head.ycor()
                        segments[0].goto(x, y)
                move()
                for segment in segments:
                        if segment.distance(head) < 20:
                                time.sleep(1)
                                head.goto(0, 0)
                                head.direction = "stop"
                                colors = random.choice(['red', 'blue', 'green'])
                                shapes = random.choice(['square', 'circle'])
                                for segment in segments:
                                        segment.goto(1000, 1000)
                                segment.clear()

                                score = 0
                                delay = 0.1
                                pen.clear()
                                pen.write("Score : {} High Score : {} ".format(
                                        score, high_score), align="center", font=("candara", 24, "bold"))
                time.sleep(delay)

        wn.mainloop()
print("!Welcome to TEAM OP's Snake Game! ")
time.sleep(5)
print()
print("You will need an strong password which we will provide with help of our encrypter to chech if you are human or not!!")
time.sleep(5)
print()
print("Make sure that you will get only 2 TRIALS to get your password right or the game will disable and you have to restart your game")
print("NOTE : Lowercase L will not be assigned in the password")
time.sleep(5)
a=str(input("Are you ready to have fun. (type yes or no)"))
if (a=="yes"):
    print("Your new encrypted password is (",password,")")
    pass_1=str(input(" Re-enter the exact same password to check that you are human and make sure of uppercase , lowercase and symbol "))
    if (password != pass_1):
        print("You have a last chance to verify. (DELAY OF 10 SEC IS BEING APPLIED)")
        time.sleep(10)
        pass_2=str(input(" Re-enter the exact same password. (INCORRECT PASSWORD MIGHT LEAD TO SHUT THE PROGRAM)"))
        if (password != pass_2):
            print("I am SORRY but verification FAILED. RESTART THE PROGRAM")
            print()
        elif (password == pass_2):
            print("HUMAN CONFIREMED")
            print("Enjoy your game")
            snake_game()
    elif (password == pass_1):
        print("HUMAN CONFIREMED")
        print("Enjoy your game")
        time.sleep(2)
        snake_game()


        
        
    




