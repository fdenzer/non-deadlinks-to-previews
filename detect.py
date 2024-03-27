import requests
# detect,if link is dead or returns code 200

def detect(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

if __name__ == "__main__":
    url = "https://mainz.scientists4future.org/"
    print(detect(url))