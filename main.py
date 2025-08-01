```python
import requests
from bs4 import BeautifulSoup

def fetch_ip_info(ip_address):
    """
    Fetches information about a given IP address using an online API.
    
    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing information about the IP address.
    """
    try:
        # API endpoint for IP information
        api_url = f'https://ipinfo.io/{ip_address}/json'
        response = requests.get(api_url)
        
        # Raise an error if the response is not successful
        response.raise_for_status()
        
        # Return the JSON response as a dictionary
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching IP information: {e}")
        return {}

def display_ip_info(ip_info):
    """
    Displays the IP address information in a readable format.

    Args:
        ip_info (dict): The dictionary containing IP information.
    """
    if ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No information available for this IP address.")

def main():
    """
    Main function to execute the script.
    """
    # Get user input for the IP address
    ip_address = input("Enter an IP address to look up: ")
    
    # Fetch and display the IP information
    ip_info = fetch_ip_info(ip_address)
    display_ip_info(ip_info)

if __name__ == "__main__":
    main()
```
