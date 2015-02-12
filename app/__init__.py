from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # return a string

@app.route('/ext')
def welcome():
    return render_template('ext.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)