import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch data")
        return []

if __name__ == "__main__":
    data = fetch_data()
    print(f"Data length: {len(data)}")
    for item in data[:5]:  # Вивести перші 5 елементів
        print(f"ID: {item['id']}, Title: {item['title']}")
