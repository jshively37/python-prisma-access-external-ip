from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

ENV = os.getenv("ENV")
API_KEY = os.getenv("API_KEY")
OUTPUT_DIR = "output/"
OUTPUT_FILE = "output.json"
URL = f"https://api.{ENV}.datapath.prismaaccess.com/getPrismaAccessIP/v2"


def fetch_prisma_access_ips():
    payload = json.dumps(
        {"serviceType": "gp_gateway", "addrType": "active", "location": "all"}
    )
    headers = {"header-api-key": API_KEY, "Content-Type": "application/json"}

    try:
        response = requests.request("POST", URL, headers=headers, data=payload)
        response.raise_for_status()
        result = response.json()
        return result.get("result", [])
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []


def format_response(data):
    _ = []
    for item in data:
        zone = item.get("zone", "unknown")
        for address_detail in item.get("address_details", []):
            _.append(
                {"region": zone, "address": address_detail.get("address")}
            )
    return _


def save_to_file(data, filename):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    output = OUTPUT_DIR + OUTPUT_FILE
    response = fetch_prisma_access_ips()
    data = format_response(response)
    save_to_file(data, output)
