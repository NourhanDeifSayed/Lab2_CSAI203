from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getvalue():
    name=request.form['name']
    age=request.form['age']
    birth_date=request.form['Dateofbirth']
    return render_template('display.html',n=name,age=age,bd=birth_date)
if __name__ == "__main__":
    app.run(debug=True)


