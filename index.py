from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

@app.route('/about')
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html', name=name)

@app.route('/api')
def api():
    responseData = {
        'id': 1,
        'name': 'ivo',
        'roles': ['admin', 'user']
    }
    return jsonify(responseData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)