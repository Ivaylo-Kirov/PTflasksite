from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/about')
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)