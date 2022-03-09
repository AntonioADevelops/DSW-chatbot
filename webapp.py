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
def user_input1():
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

    """
    if u_input in greetings and count == 2:
        count = count + 1
        reply2 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response2 = reply2)

    elif u_input not in greetings and count >= 2:
        count = count + 1
        reply2 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p>')
        return render_template('home.html', response2 = reply2)

    if u_input in greetings and count == 3:
        count = count + 1
        reply3 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response3 = reply3)

    elif u_input not in greetings and count == 3:
        count = count + 1
        reply3 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">Sorry, I don\'t quite understand. Greet me in in a different manner.</p>')
        return render_template('home.html', response3 = reply3)

    if u_input in greetings and count == 4:
        count = count + 1
        reply4 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response4 = reply4)

    elif u_input not in greetings and count == 4:
        count = count + 1
        reply4 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response4 = reply4)

    if u_input in greetings and count >= 5:
        count = count + 1
        reply5 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response5 = reply5)

    elif u_input not in greetings and count == 5:
        count = count + 1
        reply5 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response5 = reply5)
    
    if u_input in greetings and count == 6:
        count = count + 1
        reply6 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response6 = reply6)

    elif u_input not in greetings and count == 6:
        count = count + 1
        reply6 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response6 = reply6)
    
    if u_input in greetings and count == 7:
        count = count + 1
        reply7= Markup('<p class="user">') + u_input + Markup('</p><p class="bot">') + random.choice(bot_greetings) + Markup('</p>')
        return render_template('home.html', response6 = reply7)

    elif u_input not in greetings and count == 7:
        count = count + 1
        reply7 = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response6 = reply7)
    """

if __name__=="__main__":
    app.run(debug=False)
