

# make a funcion that gets a joke from the internet
def get_joke():
    import requests
    response = requests.get('https://icanhazdadjoke.com')
    if response.status_code == 200:
        return response.json()['joke']
    else:
        return "Failed to retrieve joke"


get_joke()

