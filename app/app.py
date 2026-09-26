from flask import Flask
import Items

app = Flask(__name__)

@app.route('/')
def getItems():
    items = " ".join(Items.randomizeItems())
    return items

if __name__ == '__main__':
    app.run()