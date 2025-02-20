
import requests

def get_website_content(url):
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://www.example.com"
    content = get_website_content(url)
    print(content)
