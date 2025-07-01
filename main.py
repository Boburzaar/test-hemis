import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from parse_txt import parse_txt
from parse_docx import parse_docx
from parse_json import parse_json

TOKEN = os.getenv("BOT_TOKEN", "7150073484:AAEzUvGQe5F4RK3VpK5vZMpXCZsmqK9tcDg")

app = ApplicationBuilder().token(TOKEN).build()

user_states = {}

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    doc = update.message.document
    file = await doc.get_file()
    file_path = f"{doc.file_unique_id}_{doc.file_name}"
    await file.download_to_drive(file_path)

    if file_path.endswith(".txt"):
        questions = parse_txt(file_path)
    elif file_path.endswith(".docx"):
        questions = parse_docx(file_path)
    elif file_path.endswith(".json"):
        questions = parse_json(file_path)
    else:
        await update.message.reply_text("Faqat .txt, .docx yoki .json fayl yuboring.")
        return

    user_states[update.effective_user.id] = {"questions": questions, "index": 0, "correct": 0}
    await send_next_question(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    state = user_states.get(user_id)
    if not state:
        await update.message.reply_text("Iltimos, test faylini yuboring.")
        return

    current_q = state["questions"][state["index"] - 1]
    if update.message.text.strip().upper() == current_q["answer"].upper():
        state["correct"] += 1
        await update.message.reply_text("✅ To‘g‘ri")
    else:
        await update.message.reply_text(f"❌ Noto‘g‘ri. To‘g‘ri javob: {current_q['answer']}")

    await send_next_question(update, context)

async def send_next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    state = user_states[user_id]
    index = state["index"]

    if index >= len(state["questions"]):
        total = len(state["questions"])
        correct = state["correct"]
        await update.message.reply_text(f"Test tugadi.
To‘g‘ri javoblar soni: {correct}/{total}")
        user_states.pop(user_id)
        return

    q = state["questions"][index]
    state["index"] += 1

    variants = "\n".join([f"{opt}) {val}" for opt, val in zip(["A", "B", "C", "D"], q["options"])])
    await update.message.reply_text(f"{q['question']}

{variants}")

app.add_handler(MessageHandler(filters.Document.ALL, handle_document))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == "__main__":
    app.run_polling()
