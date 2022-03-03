from urllib import response
from flask import Flask, url_for, render_template, request, Markup
import markupsafe

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

greetings = ['hi', 'Hi', 'hello', 'Hello', 'greetings', 'Greetings', 'howdy', 'Howdy', 'hey', 'Hey']

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def user_input():
    u_input = request.args['response']
    if u_input in greetings:
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> Hello, I\'m a Chat Bot. Ask me a question and I\'ll try my best to answer!</p>')
        return render_template('home.html', response = reply)
    else:
        reply = Markup('<p class="user">') + u_input + Markup('</p><p class="bot"> "Sorry, I don\'t quite understand. Ask me something else."</p>')
        return render_template('home.html', response = reply)
    
@app.route("/update")
def render_update():
    print("hi")
    
    
if __name__=="__main__":
    app.run(debug=False)
