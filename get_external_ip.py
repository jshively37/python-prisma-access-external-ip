from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

ENV = os.environ.get("ENV")
API_KEY = os.environ.get("API_KEY")


url = f"https://api.{ENV}.datapath.prismaaccess.com/getPrismaAccessIP/v2"

payload = json.dumps(
    {"serviceType": "gp_gateway", "addrType": "active", "location": "all"}
)
headers = {"header-api-key": API_KEY, "Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=payload).json()

for response in response.get("result", []):
    for address in response.get("address_details", []):
        print(address.get("address"))
