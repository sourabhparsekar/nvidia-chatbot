import json

# Load your dataset
def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    texts = []
    for item in data["questions"]:
        category = item["category"]
        question = item["question"]
        answer = item["answer"]
        texts.append(f"{category} \n {question} \n {answer}")

    return texts


# Load your data
data = load_data("docs\Legal_contract_QA.json")
