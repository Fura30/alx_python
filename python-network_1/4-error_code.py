"""
Sends a request to a URL and displays the response body. Prints an error message with
the HTTP status code if the status code is greater than or equal to 400.
"""

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Display the response body
    print(response.text)
    
    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)

if __name__ == "__main__":
    main()
