from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('home-banking.html')

if __name__ == '__app__':
    app.run(debug=True)   
    
