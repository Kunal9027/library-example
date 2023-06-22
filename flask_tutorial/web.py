from flask import Flask ,redirect , url_for ,render_template , request
app = Flask(__name__)

@app.route('/')              #@app.route( ) is used to give a specific path for our site 
def home():
    return render_template("index.html") # render templates  it help to use/render template from other folders



if __name__=="__main__":
    app.run(debug=True) 

# when we use debug=True it auto start the server after adding new changes but never use this while your server is also used by some one else
# port is used to change port of the web site 
