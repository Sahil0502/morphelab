from flask import Flask
import subprocess
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Retrieve system username
    username = os.getenv("USER", "Unknown User")

    # Get server time in IST
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    # Run the 'top' command to get system information
    top_output = subprocess.check_output("top -b -n 1", shell=True).decode('utf-8')

    # Display output in HTML format
    return f"""
    <h2>Name: Sahil Singh</h2>
    <h3>User: {username}</h3>
    <h4>Server Time: {server_time}</h4>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
