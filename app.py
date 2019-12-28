from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Shaikh loves contributing to ScoreLab.'


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
