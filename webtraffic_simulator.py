import requests
import time

def simulate_visits(url, visit_count, delay=1):
    """
    Simulates visits to a given URL.

    Parameters:
        url (str): The website URL to visit.
        visit_count (int): The number of simulated visits.
        delay (int): Delay between visits in seconds.
    """
    for i in range(visit_count):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Visit {i+1} to {url} was successful.")
            else:
                print(f"Visit {i+1} failed with status code: {response.status_code}")
            time.sleep(delay)  # Pause between requests
        except requests.exceptions.RequestException as e:
            print(f"Error during visit {i+1}: {e}")

def main():
    url = input("Enter the website URL to visit: ")
    visit_count = int(input("Enter the number of visits to simulate: "))
    delay = int(input("Enter the delay between visits (in seconds): "))
    
    simulate_visits(url, visit_count, delay)

if __name__ == "__main__":
    main()
