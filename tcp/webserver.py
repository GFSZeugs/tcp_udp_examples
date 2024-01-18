from flask import Flask
import sys

if len(sys.argv) != 2:
    print("usage: python webserver.py <PORT>")
    exit()

PORT = int(sys.argv[1])

app = Flask(__name__)

@app.route("/")
def root():
    return """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Beispiel Webseite</title>
    </head>
    <body>
        <h1>Ich bin ein Beispiel!</h1>
    </body>
</html>
"""

app.run("0.0.0.0", port=PORT)
