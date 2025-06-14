import subprocess
import threading

def run_bot():
    subprocess.run(["python", "main.py"])

def run_ui():
    subprocess.run(["python", "web/web_ui.py"])

bot_thread = threading.Thread(target=run_bot)
ui_thread = threading.Thread(target=run_ui)

bot_thread.start()
ui_thread.start()

bot_thread.join()
ui_thread.join()