from urllib import response
from flask import Flask, url_for, render_template, request, Markup
import markupsafe 
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = ['hi', 'Hi', 'hello', 'Hello', 'greetings', 'Greetings', 'howdy', 'Howdy', 'hey', 'Hey']

bot_greetings = ['Hey! I\'m HelloBot.', 'Greetings User! My Name\'s HelloBot.', 'Howdy Partner! I go by HelloBot.']

u_input_list = []

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def user_input():
    u_input = request.args['response']
    
    if u_input in greetings:
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(bot_greetings) + Markup('</p><br>')
        return render_template('home.html', response = reply)
    
    else:
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p><br>')
        return render_template('home.html', response = reply)
    
def update_chat():
    update = request.args['storedData']
    return render_template('home.html', Markup('<p class="user">') + update + Markup("</p><br>))

if __name__=="__main__":
    app.run(debug=False)
