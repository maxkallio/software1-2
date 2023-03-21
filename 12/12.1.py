import requests

# Make a GET request to the API to fetch a random joke
response = requests.get("https://api.chucknorris.io/jokes/random")

# Extract the JSON data from the response
data = response.json()

# Extract the joke text from the JSON data
joke_text = data["value"]

# Print the joke text to the user
print(joke_text)