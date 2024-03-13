from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    # Pass data to the template
    message = 'Hello, World!'
    return render_template('index.html', message=message)

@app.route('/gg')
def idk_wtf():
    param = request.args.get('mail')
    return param

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)