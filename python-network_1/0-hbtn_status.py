import requests

def fetch_and_display_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json() if response.headers['Content-Type'] == 'application/json' else response.text

        if isinstance(data, dict):
            for key, value in data.items():
                print(f"- {key}: {value}")
        else:
            print(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(url)
 
