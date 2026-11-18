from flask import Flask,request, render_template

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    print(request.method)
    # print(request.form)
    if request.method=='POST':
        with open('file.txt','a') as f:
            f.write(f"The name is {request.form['name']} and the email is {request.form['email']}.\n")
    return render_template('contact.html')

app.run(debug=True)