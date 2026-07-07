def run(expression: str):
    print("[Expression]:", expression)
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "계산 오류"