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
        reply = Markup('<p class="container darker">') + u_input + Markup('</p><p class="container"> Hello, I\'m a Chat Bot. Ask me a question and I\'ll try my best to answer!</p>')
        return render_template('home.html', response = reply)
    else:
        return render_template('home.html', bot_response1 = "Sorry, I don't quite understand. Ask me something else.", user_response1 = u_input)
     
if __name__=="__main__":
    app.run(debug=False)
