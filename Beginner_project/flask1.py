from flask import Flask,render_template
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html",data=[1,2,3,45])
@app.route("/about")
def about():
    return "welcome to about page"
@app.route("/profile/<name>")
def profile(name):
    return "hello "    +   str(name)
@app.route("/profile/<int:id>")
def profile2(id):
    return "your requested user with id  " + str(id)


if __name__=="__main__":
    app.run(debug = True)
 