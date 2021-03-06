from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    return render_template("compliment.html",
                           person=player)

@app.route('/game')
def show_madlib_form():
    """show the game form"""

    play = request.args.get("play")

    if play == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """show madlib"""

    color = request.args.get("color")
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    food = request.args.getlist("food")

    all_foods = " and ".join(food)


    return render_template("madlib.html",
                           person=person,
                           noun=noun,
                           adjective=adjective,
                           color=color,
                           food=all_foods)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
