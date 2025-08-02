```python
import requests
from bs4 import BeautifulSoup
import csv

def fetch_ip_info(ip_address):
    """
    Fetches information about a given IP address from an online API.
    
    Args:
    ip_address (str): The IP address to lookup.
    
    Returns:
    dict: A dictionary containing IP information.
    """
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for IP: {ip_address}")
        return None

def save_to_csv(data, filename='ip_info.csv'):
    """
    Saves the fetched IP information to a CSV file.
    
    Args:
    data (list): A list of dictionaries containing IP information.
    filename (str): The name of the CSV file to save data.
    """
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main():
    """
    Main function to execute the OSINT project.
    """
    ip_addresses = ['8.8.8.8', '1.1.1.1', '192.168.1.1']  # Example IP addresses
    ip_info_list = []
    
    for ip in ip_addresses:
        ip_info = fetch_ip_info(ip)
        if ip_info:
            ip_info_list.append(ip_info)

    if ip_info_list:
        save_to_csv(ip_info_list)
        print(f"IP information saved to 'ip_info.csv'.")

if __name__ == "__main__":
    main()
```