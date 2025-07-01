def parse_txt(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = content.split("+++++")
    questions = []
    for block in blocks:
        lines = [l.strip() for l in block.strip().split("=====") if l.strip()]
        if len(lines) < 4:
            continue
        answer_line = [l for l in lines if l.startswith("#")]
        if not answer_line:
            continue
        answer_text = answer_line[0].lstrip("#").strip()
        all_options = [l.lstrip("#").strip() for l in lines[1:5]]
        correct_index = all_options.index(answer_text)
        questions.append({
            "question": lines[0],
            "options": all_options,
            "answer": ["A", "B", "C", "D"][correct_index]
        })
    return questions
