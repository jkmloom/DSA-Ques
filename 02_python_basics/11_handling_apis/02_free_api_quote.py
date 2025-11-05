import requests

def fetch_random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    result = requests.get(url)
    data = result.json()

    if data['success'] and 'data' in data:
        quote = data['data']
        quote_content = quote['content']
        quote_author = quote['author']
        return quote_content, quote_author
    else:
        raise Exception("Failed to fetch quote!")
    
def main():
    try:
        content, author = fetch_random_quote()
        print(f"Content: {content}")
        print(f"Author: {author}")
    except Exception as exc:
        print(str(exc))

if __name__ == "__main__":
    main()