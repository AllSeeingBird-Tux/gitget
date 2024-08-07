import requests

a = input("Enter a search term: ")

b = input("Enter a Language: ")

url = f'https://github.com/search?q={a}&type=repositories+language%3AC&type=repositories&l={b}'

x = requests.get(url)
print(x.text)
