from os import getenv
from dotenv import load_dotenv
load_dotenv()


URL = getenv('URL')
DOMAIN = getenv('DOMAIN')

HEADERS = {
    "User-Agent":
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.1.1148 (beta) Yowser/2.5 Safari/537.36"
}