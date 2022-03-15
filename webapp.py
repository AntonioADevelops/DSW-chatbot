from flask import Flask, url_for, render_template, request, Markup
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = ['Hi', 'Hello', 'Greetings', 'Howdy', 'Hey', 'Sup', 'Whats Good', 'Wassup',]

bot_greetings = ['Hey! I\'m HelloBot.', 'Greetings User! My Name\'s HelloBot.', 'Howdy Partner! I go by HelloBot.']

confused = ['Sorry, I don\'t quite understand. Say it in a different way.', 'I didnt quite catch that. Please rephrase your sentence.', 'I haven\'t learned what that means, please ask in a different manner.']

u_how_are_you = ['How are you?', 'How are you?', 'How do you do', 'How do you do?', 'How do you feel today?', 'How do you feel today?']
 
b_how_are_you = ['I\'m doing pretty good.']

u_origin_who = ['Who made you', 'Who made you?', 'Who created you', 'Who created you?']

b_origin_who = ['I was developed by Antonio A. for a school project.']

u_origin_how = ['How were you created', 'How were you created?', 'How were you made', 'How were you made?']

b_origin_how = ['I was born from code! My creator spent countless hours copying and pasting code from stackoverflow until I worked.']


@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")

def user_input():
    u_input = request.args['response']
    chat_update = request.args["storedData"]
    update = Markup(chat_update)
        
    if u_input.upper() in (name.upper() for name in greetings):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(bot_greetings) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input.upper() in (name.upper() for name in u_how_are_you):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_how_are_you) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input.upper() in (name.upper() for name in u_origin_who):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_origin_who) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input.upper() in (name.upper() for name in u_origin_how):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_origin_how) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input not in greetings:
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(confused) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)

if __name__=="__main__":
    app.run(debug=False)
