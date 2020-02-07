import requests
import sys
from datetime import datetime


# I DO NOT recommend this version for reserving html files
def main():
    url = None
    if len(sys.argv) < 2:
        print("Switching to input mode...")
        url = input("URL to scrape: ")
    elif len(sys.argv) > 2:
        print("Re-implement adding of multiple urls")
        exit(1)
    time = str(datetime.now().time())[:-7]
    date = str(datetime.now().date()).replace("-", "")
    returned = requests.get(url)
    result = str(returned.content)
    stamp = str(f"{date}_{time}")
    with open(f"scrapped_files/{stamp}.html", "a+") as f:
        f.write(result)


if __name__ == '__main__':
    main()
