from flask import Flask
import os
import dotenv

app = Flask(__name__)
dotenv.load_dotenv()

@app.route('/')
def hello_world():
    return "Welcome to E Grades Book"

if __name__ == '__main__':
    app.run(port=os.environ.get("PORT"))
