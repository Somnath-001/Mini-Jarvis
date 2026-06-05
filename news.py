import requests

newsapi_key = "d7d40341ebf140e2bd42921a4ee6d43c" 
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}"
response = requests.get(url)
if( response.status_code == 200):
    data = response.json()
    articles = data.get("articles",[])
    for i,article in enumerate(articles):
        print(f"Title {i}: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"Link: {article['url']}")
        print(f"Content: {article['content']}")
        print("")

# print([i.get('author','no name') for i in articles])






