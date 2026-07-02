MODEL_8 = "qwen3:8b"
MODEL_14 = "qwen3:14b"

OLLAMA_URL = "http://localhost:11434"

def GetModel(ver: int):
	if (ver == 8):
		return MODEL_8
	if (ver == 14):
		return MODEL_14
	return MODEL_8
