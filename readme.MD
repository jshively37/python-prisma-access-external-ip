# Prisma Access Get External IP Addresses

This Python script will return the Prisma Access active GP gateway addresses to a JSON file.

# Requirements

```
certifi==2025.1.31
charset-normalizer==3.4.1
idna==3.10
python-dotenv==1.1.0
requests==2.32.3
urllib3==2.4.0
```

# Installing and executing

Clone down this repo and cd into the directory.

Create a Python virtual environment: `python -m venv venv`

Activate the virtual environment: \
    Windows: `.\venv\Scripts\activate` \
    OSX: `source venv/bin/activate`

Install the dependencies using `pip install -r requirements.txt`

Rename .env.example to .env and populate your variables in this file. The .env is included in the .gitignore to ensure it does not accidently get checked into a git repo.

Run: `python main.py`

The output will be written to the directory and file defined in the `OUTPUT_DIR` and `OUTPUT_FILE` variables as JSON.
