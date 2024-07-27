import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def main():
    configure()
    url = f"http://www.omdbapi.com/?i=tt3896198&apikey={os.getenv('api_key')}"
    response = requests.get(url)


main()
