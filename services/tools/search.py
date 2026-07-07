import requests
import config

def run(query:str):
    r = requests.post(
        "https://google.serper.dev/search",
        headers={
            "X-API-KEY": config.SERPER_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "q": query,
            "num": 5
        },
        timeout=10
    )

    r.raise_for_status()

    data = r.json()

    return [
        {
            "title": item["title"],
            "url": item["link"],
            "snippet": item["snippet"]
        }
        for item in data.get("organic", [])
    ]

    # print("[QUERY]:", query)
    # results = []

    # with DDGS() as ddgs:
    #     for r in ddgs.text(
    #         query,
    #         backend="google",
    #         max_results=5
    #     ):
    #         results.append({
    #             "title": r["title"],
    #             "url": r["href"],
    #             "snippet": r["body"]
    #         })

    # return results