from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/co2_filtered.csv')
def data():
    return jsonify({'results'})


if __name__ == '__main__':
    app.run(debug=True)