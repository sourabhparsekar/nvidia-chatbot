from flask import Flask, request
from execution_plan import rag_chain

app = Flask(__name__)


# Run the chatbot
@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    question = data.get("question")
    # print(question)
    # Run the conversation chain with the user's question
    # response = conversation.run(question)
    chat_history = []  # Collect chat history here (a sequence of messages)
    response = rag_chain.invoke({"input": question, "chat_history": chat_history})
    response_str = str(response)
    response_str = response_str.replace("), Document(", "}, {")
    response_str = response_str.replace("Document(", "{")
    response_str = response_str.replace(")], 'answer'", "}, 'answer'")

    # print(response_str)
    return response_str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
