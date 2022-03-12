from turtle import update
from urllib import response
from flask import Flask, url_for, render_template, request, Markup
import markupsafe 
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = ['Hi', 'Hello', 'Greetings', 'Howdy', 'Hey', 'Sup', 'Whats Good', 'Wassup',]

bot_greetings = ['Hey! I\'m HelloBot.', 'Greetings User! My Name\'s HelloBot.', 'Howdy Partner! I go by HelloBot.']

confused = ['Sorry, I don\'t quite understand.', 'I didnt quite catch that. Please rephrase your greeting.', 'I haven\'t learned that greeting, please ask in a different manner.']


@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")

def user_input():
    u_input = request.args['response']
    chat_update = request.args["storedData"]
        
    if u_input.upper() in (name.upper() for name in greetings):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(bot_greetings) + Markup('</p><br>')
        update = Markup(chat_update)
        return render_template('home.html', response = update + reply)
    
    elif u_input not in greetings:
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(confused) + Markup('</p><br>')
        update = Markup(chat_update)
        return render_template('home.html', response = update + reply)

if __name__=="__main__":
    app.run(debug=False)
