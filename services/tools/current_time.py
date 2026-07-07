from datetime import datetime

def run(expression: str = ""):
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")