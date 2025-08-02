```python
import requests
from bs4 import BeautifulSoup

def fetch_ip_info(ip_address):
    """
    Fetches information about the given IP address from an online API.
    
    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing information about the IP address.
    """
    try:
        # URL to fetch IP information
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {ip_address}: {e}")
        return None

def display_ip_info(ip_info):
    """
    Displays the IP information in a readable format.
    
    Args:
        ip_info (dict): The IP information to display.
    """
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No information available.")

def main():
    # Example IP address to investigate
    ip_address = input("Enter an IP address to investigate: ")
    
    # Fetching the IP information
    ip_info = fetch_ip_info(ip_address)
    
    # Displaying the fetched information
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
