from services.tools import calculator
from services.tools import current_time
from services.tools import search
from services.tools import naver_news

TOOLS = {
    "calc": {
        "func": calculator.run,

        "ollama": {
            "type": "function",

            "function": {
                "name": "calc",

                "description": "수식을 계산한다.",

                "parameters": {
                    "type": "object",

                    "properties": {
                        "expression": {
                            "type": "string"
                        }
                    },

                    "required": [
                        "expression"
                    ]
                }
            }
        }
    },
    "current_time": {
        "func": current_time.run,

        "ollama": {
            "type": "function",

            "function": {
                "name": "current_time",

                "description": """
                    현재 시스템 시간을 반환한다.

                    무언가를 검색(search)하기 전 반드시 현재 시각을 미리 확인한다.
                    """,

                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "expression"
                    ]
                }
            }
        }
    },
    "search": {
        "func": search.run,

        "ollama": {
            "type": "function",

            "function": {
                "name": "search",

                "description": """
                    인터넷에서 정보를 검색한다.

                    한 번의 검색으로 충분한 정보를 얻도록
                    최대한 구체적인 검색어를 작성한다.

                    검색 결과를 받은 뒤에는
                    추가 검색하지 말고
                    반드시 결과를 이용하여 답변한다.
                    """,

                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "검색할 내용"
                        }
                    },
                    "required": [
                        "query"
                    ]
                }
            }
        }
    },
    "naver_news": {
        "func": naver_news.run,

        "ollama": {
            "type": "function",

            "function": {
                "name": "naver_news",

                "description": """
                    인터넷에서 뉴스를 검색한다.

                    한 번의 검색으로 충분한 정보를 얻도록
                    최대한 구체적인 검색어를 작성한다.

                    검색 결과를 받은 뒤에는
                    추가 검색하지 말고
                    반드시 결과를 이용하여 답변한다.
                    """,

                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "검색할 내용"
                        }
                    },
                    "required": [
                        "query"
                    ]
                }
            }
        }
    }
}

def run(tool: str, arguments: str):
    tool_info = TOOLS.get(tool)
    print("tool manager-tool:", tool, "arguments:", arguments)
    if tool_info is None:
        return None

    return {
        "tool": tool,
        "success": True,
        "content": tool_info["func"](**arguments)
    }

def get_ollama_tools():
    return [
        tool["ollama"]
        for tool in TOOLS.values()
    ]