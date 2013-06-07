# imports
from flask import Flask, render_template
 
# run the app
app = Flask(__name__)
 
# route for domain
@app.route("/")
# route function (get)
def hello():
	return render_template('index.html')
    # return "Hello World!"
 
# main (runs python file)
if __name__ == "__main__":
    app.run()