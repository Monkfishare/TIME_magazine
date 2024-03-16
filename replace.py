recipe_path = "time_magazine.recipe"

Edition_ID = "6133140"
# For past edition, for example, Edition_ID = '6548003'
# https://raw.githubusercontent.com/Monkfishare/TIME_magazine/main/TIME_magazine_database.txt

with open(recipe_path, 'r', encoding='utf-8') as file:
    recipe_content = file.read()

modifications = {
    "self.cover_url = data['hero']['src']['large']": "self.cover_url = data['hero']['src']['large'] + '?quality=100&w=3000'",
    "cover_url = article['hero']['src']['large']": "cover_url = article['hero']['src']['large'] + '?quality=100&w=3000'",
    "img['src'] = img['data-lazy-src']": "img['src'] = img['data-lazy-src'] + '?quality=100&w=1000'",
    "url = article['shortlink']": "url = article['shortlink'].replace('?p=', '')",
    "https://time.com/magazine": f"https://time.com/magazine/us/{Edition_ID}"
}

modified_content = recipe_content
for original, replacement in modifications.items():
    modified_content = modified_content.replace(original, replacement)

with open('time_magazine.recipe', 'w', encoding='utf-8') as file:
    file.write(modified_content)
