# requests library: Requests is a simple, yet elegant, HTTP library.
# requests url: https://pypi.org/project/requests/

import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return username, user_country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        usrename, user_country = fetch_random_user_freeapi()
        print(f"Username: {usrename}\nCountry: {user_country}")
    except Exception as exc:
        print(str(exc))

# __dunder_method__
if __name__ == "__main__":
    main()