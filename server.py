from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
     footer_year = datetime.now().year
     return render_template("index.html", ye=footer_year)



if __name__ == "__main__":
    app.run(debug=True)
