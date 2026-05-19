from flask import Flask
from flask import render_template
from flask import request
from flask import Response

from src.graph import graph

app = Flask(__name__)

history = []


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/chat",
    methods=["POST"]
)
def chat():

    user_input = request.json[
        "message"
    ]

    response = graph.invoke({

        "question":
        user_input,

        "history":
        history
    })

    answer = response[
        "answer"
    ]

    history.append({

        "user":
        user_input,

        "assistant":
        answer
    })

    def generate():

        words = answer.split()

        for word in words:

            yield word + " "

    return Response(
        generate(),
        mimetype="text/plain"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )