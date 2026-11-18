from flask import Flask,render_template

# app = Flask(__name__,static_url_path='/public')#this is how we can change the static url path
# app = Flask(__name__,static_folder='assets')#this is how we change static folder location
app = Flask(__name__,static_folder='assets',static_url_path='/public')
@app.route("/")
def hello_world():
    return render_template('index.html')

app.run(debug=True)