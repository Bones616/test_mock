import requests

def get_joke() :
    url = 'https://api.chucknorris.io/jokes/random'

    try:
       response = requests.get(url, timeout=10)
       response.raise_for_status()

    except requests.exceptions.Timeout:
        return 'No jokes'

    except requests.exceptions.ConnectionError:
         return 'HTTPError was raised'

    else:
        joke = response.json()['value']
    return joke

def len_joke() :
    joke = get_joke()
    return len(joke)

if __name__== '__main__':
    print(get_joke())


