import requests
import config

def run(query: str):
    headers = {
        "X-Naver-Client-Id": config.NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": config.NAVER_CLIENT_SECRET
    }
    params={
        "query": query,
        "display": 5,     # 가져올 뉴스 개수
        "sort": "date"    # 최신순 ("sim"은 정확도순)
    }
    r = requests.get(
        "https://openapi.naver.com/v1/search/news.json",
        headers=headers,
        params= params,
        timeout=5
    )
    r.raise_for_status()
    return r.json()