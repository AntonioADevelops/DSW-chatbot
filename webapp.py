from urllib import response
from flask import Flask, url_for, render_template, request, Markup
import markupsafe 
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = ['hi', 'Hi', 'hello', 'Hello', 'greetings', 'Greetings', 'howdy', 'Howdy', 'hey', 'Hey']

bot_greetings = ['Hey! I\'m HelloBot.', 'Greetings User! My Name\'s HelloBot.', 'Howdy Partner! I go by HelloBot.']

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def user_input():
    u_input = request.args['response']
    count = 1
    
    if u_input in greetings and count == 1:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(bot_greetings) + Markup('</p><br>')
        return render_template('home.html', response1 = reply)
    
    elif u_input not in greetings and count == 1:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p><br>')
        return render_template('home.html', response1 = reply)
@app.route("/update")
def scroll_chat():
    print("hi")
    """
    if u_input in greetings and count == 2:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response2 = reply)
    
    elif u_input not in greetings and count == 2:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p>')
        return render_template('home.html', response2 = reply)
    
    if u_input in greetings and count == 3:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response3 = reply)
    
    elif u_input not in greetings and count == 3:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p>')
        return render_template('home.html', response3 = reply)
    
    if u_input in greetings and count == 4:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response4 = reply)
    
    elif u_input not in greetings and count == 4:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response4 = reply)
    
    if u_input in greetings and count == 5:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response5 = reply)
    
    elif u_input not in greetings and count == 5:
        count = count + 1
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response5 = reply)
    """
    
if __name__=="__main__":
    app.run(debug=False)
