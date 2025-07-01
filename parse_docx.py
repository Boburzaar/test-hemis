from docx import Document
from parse_txt import parse_txt

def parse_docx(path):
    doc = Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    temp_txt = path + ".temp.txt"
    with open(temp_txt, "w", encoding="utf-8") as f:
        f.write(text)
    return parse_txt(temp_txt)
