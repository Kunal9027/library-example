from flask import Flask ,redirect , url_for ,render_template
app = Flask(__name__)

@app.route('/')              #@app.route( ) is used to give a specific path for our site 
def home():
    return render_template("index.html") # render templates  it help to use/render template from other folders


@app.route('/doc')               
def document():
    return render_template("base.html")





@app.route('/hello')
def hello():
    return '<h1>Jai Shree Ram<h1> \n hello its page 2 '

@app.route('/admin')
def admin():
    return redirect(url_for("hello"))  # redirect & url_for is used to redirect user from 1 url to other


if __name__=="__main__":
    app.run(debug=True) 
# when we use debug=True it auto start the server after adding new changes but never use this while your server is also used by some one else
# port is used to change port of the web site 