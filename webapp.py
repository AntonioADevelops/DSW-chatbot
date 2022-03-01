from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/form")
def userinput():
    input = request.args['response']
    if input == "hi":
        return render_template('home.html', textoutput = "Hello Im a Chat Bot")
     
if __name__=="__main__":
    app.run(debug=False)
