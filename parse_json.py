import json

def parse_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = []
    for item in data:
        question = item["savol"]
        options = item["variantlar"]
        answer = item["javob"]
        correct_index = options.index(answer)
        questions.append({
            "question": question,
            "options": options,
            "answer": ["A", "B", "C", "D"][correct_index]
        })
    return questions
