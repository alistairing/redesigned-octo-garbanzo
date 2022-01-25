import pandas as pd
import requests
import json

# set the target url
target_url = "http://openrecipes.s3.amazonaws.com/openrecipes.txt"

# get the JSON style content
response = requests.get(target_url)
content = response.text

# clean the content so that it can be converted by json.loads() function
# 1) enclose with square brackets
# 2) insert commas after each } 
# 3) remove final comma
data = '['+ content + ']'
data = data.replace("}", "},")
data = data[:-3]+data[-2:]

# convert from string of json format into python object 
data_json = json.loads(data)

# convert into dataframe
df = pd.DataFrame(data_json)
print(df.head())

# Example Query
# Which recipes contain mushrooms in the name
mushrooms = df[df["name"].str.contains("Mushroom")]
print('\n\nRecipes with mushrooms in the title: ', mushrooms)

# Which recipes contain mushrooms as ingredient
mushrooms = df[df["ingredients"].str.contains("Mushrooms")]
print('\n\nRecipes with mushrooms as ingredient: ', mushrooms)



