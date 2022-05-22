from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:word_to_repeat>/<int:num_of_repeats>')
def hello(num_of_repeats, word_to_repeat):
    return render_template('hello.html', num = num_of_repeats, word = word_to_repeat)
if __name__ == "__main__":
    app.run(debug=True, port=5001)