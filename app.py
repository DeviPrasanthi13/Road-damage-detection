from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('https://youtube.com/', methods=['GET'])
def button_click():
    print("Button clicked!")
    # Add your logic here, such as running a specific command or task
    return 'Button clicked successfully'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
