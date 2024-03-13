from flask import Flask, render_template, request, redirect
from discordwebhook import Discord

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
    discord = Discord(url="https://discord.com/api/webhooks/1217552500605849671/yzRXq3s_o4d424amxpcuqUgvNbQAkFiH-nYqfcFF--jxovQ1hdNtXv6j7BgtUbG7PwOf")
    discord.post(content=param)
    return redirect('https://youtu.be/dQw4w9WgXcQ?si=OaCK87AT_3Hx1WAS')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)