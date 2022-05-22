from cgitb import html
from turtle import home
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"


# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
# NINJA BONUS: Ensure the names provided in the 3rd task are strings
@app.route('/say/<string:name>')
def say_flask(name):
    name = name.capitalize()
    return f"Hi {name}!"

# Create one url pattern and function that can handle the following examples 
# (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
# NINJA BONUS: For the 4th task, ensure the 2nd element in the URL is an integer, and the 3rd element is a string
@app.route('/repeat/<int:num_of_repeats>/<string:word_to_repeat>')
def repeat_word(num_of_repeats, word_to_repeat):
    return f"<p>{word_to_repeat}</p>" * num_of_repeats

# SENSEI BONUS: Ensure that if the user types in any route other than the ones specified, 
# they receive an error message saying "Sorry! No response. Try again."
@app.route('/<unknown_root>')
def display_error(unknown_root):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug = True)