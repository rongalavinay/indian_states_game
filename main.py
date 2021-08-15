import turtle
import pandas

screen=turtle.Screen()
screen.title('india map pointer')
image='map.gif'
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv('states of india.csv')
states=data['states'].to_list()
game_is_on=True
correct_guess=0
guessed_states=[]

while game_is_on:
    guess=screen.textinput(title=f'{correct_guess}/29 GUESS THE STATES OF INDIA', prompt='Guess The Next State Of India')

    if guess=='exit':
        game_is_on=False
    if guess in states:
        guessed_states.append(guess)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data['states']==guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
        correct_guess+=1
    if correct_guess>=29:
        game_is_on=False

not_guessed=[n for n in states if n not in guessed_states]

print(not_guessed)
n_guess=pandas.DataFrame(not_guessed)
n_guess.to_csv('states not guessed.csv')


