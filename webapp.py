from flask import Flask, url_for, render_template, request, Markup
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = [
    'Hi',
    'Hello',
    'Greetings',
    'Howdy',
    'Hey',
    'Sup',
    'Whats Good',
    'What\'s Good',
    'Wassup',
    'Hi.',
    'Hello.',
    'Greetings.',
    'Howdy.',
    'Hey.',
    'Sup.',
    'Whats Good.',
    'What\'s Good.',
    'Wassup.',
    'Hi!',
    'Hello!',
    'Greetings!',
    'Howdy!',
    'Hey!',
    'Sup!',
    'Whats Good!',
    'What\'s Good!',
    'Wassup!',
    'Yo',
    'Yo.',
    'Yo!']

bot_greetings = ['Hey! I\'m HelloBot.', 'Greetings User! My Name\'s HelloBot.', 'Howdy Partner! I go by HelloBot.']

u_how_are_you = ['How are you', 'How are you?', 'How do you do', 'How do you do?', 'How do you feel today?', 'How do you feel today?']
 
b_how_are_you = ['I\'m doing pretty good.']

u_who = ['Who are you', 'Who are you?', 'Who are you!',]

b_who = [' I\'m ChatBot. I can do simple conversation! Say something to me and I\'ll try to respond.']

u_origin_who = ['Who made you', 'Who made you?', 'Who created you', 'Who created you?', 'Who is your maker', 'Who is you maker?', 'Who is your creator', 'Who is you creator?', ]

b_origin_who = ['I was developed by Antonio A.']

u_why = ['Why were you made', 'Why we\'re you made', 'Why were you made?', 'Why we\'re you made?', 'What is your purpose', 'What is your purpose?', 'What\'s your purpose', 'What\'s your purpose?']

b_why = ['I am a school project.']

u_origin_how = ['How were you created', 'How were you created?', 'How were you made', 'How were you made?']

b_origin_how = ['I was born from code! My creator spent hours looking through stackoverflow forums to get me to work.']

u_eat = ['Do you eat', 'Do you eat?', 'Do you eat anything', 'Do you eat anything?', 'What do you eat', 'What do you eat?']

b_eat = ['I don\'t eat anything. I\'m not real!']

confused = ['Sorry, I don\'t quite understand. Say it in a different way.', 'I didnt quite catch that. Please rephrase your sentence.', 'I haven\'t learned what that means, please ask in a different manner.']


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
    
    elif u_input.upper() in (name.upper() for name in u_why):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_why) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input.upper() in (name.upper() for name in u_who):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_who) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    elif u_input.upper() in (name.upper() for name in u_eat):
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(b_eat) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)
    
    else:
        reply = Markup('<p class="user">') + u_input + Markup('</p><br><p class="bot">') + random.choice(confused) + Markup('</p><br>')
        return render_template('home.html', response = update + reply)

if __name__=="__main__":
    app.run(debug=False)
