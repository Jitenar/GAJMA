
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    topics = [
        "History of Machine Learning",
        "Learning Roadmap",
        "Data Preprocessing",
        "Train/Test Split",
        "Feature Scaling",
        "Linear Regression",
        "Decision Trees",
        "Random Forest",
        "Voting Classifier",
        "TPOT AutoML"
    ]
    return render_template("index.html", topics=topics)

if __name__ == "__main__":
    app.run(debug=True)

