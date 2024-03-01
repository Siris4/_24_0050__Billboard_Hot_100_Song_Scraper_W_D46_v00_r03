import requests
from bs4 import BeautifulSoup

# CONSTANTS:
LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE = 5

user_date_input = input(f"Which year do you want to Time Travel to? Please type the date in this format: YYYY-MM-DD: ")

# TODO: Formatting the date to supply to the end of the main endpoint:
# https://www.billboard.com/charts/hot-100/1989-07-01/
print(user_date_input)


response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date_input}/")   #removed: 1989-07-01
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser') #pick one or the other
# soup = BeautifulSoup(html_doc, 'lxml')
# print(soup)

song_list_for_user_picked_date = []

song_title = soup.find("h3", class_="c-title").getText(strip=True)  #removed: , limit=LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE)    #also, this gets moved to the for loop below: .getText(strip=True)
# song_rows = find_all getText

# artist_name = soup.find("p", class_="c-tagline  a-font-primary-l a-font-primary-m@mobile-max lrv-u-color-black u-color-white@mobile-max lrv-u-margin-tb-00 lrv-u-padding-t-025 lrv-u-margin-r-150", limit=LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE)
#artist_rows = find_all getText

# for title in song_titles:
#     song_title_name_text = title.getText(strip=True)
#     song_list_for_user_picked_date.append(song_title_name_text)
    # song_list_for_user_piced_date.append(song_title.text)
    # song_list_for_user_piced_date.append((artist_rows))

# print(f"Testing the song list: \n {song_list_for_user_picked_date}")

print("Song Title:")
print(f"{song_title}\n")

####################################



response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_date_input}/")
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# Initialize list to hold artist names
artist_names_list_for_user_picked_date = []

# Use find_all to get all artist names on the page
# Adjusted class to match your artist block class names
artist_names = soup.find_all("span", class_="c-label", limit=LIMIT_OF_MAXIMUM_SONGS_TO_DATA_SCRAPE)

def contains_number(value):
    # Check if the given string contains any digit
    return any(char.isdigit() for char in value)

for artist_name in artist_names:
    artist_name_text = artist_name.getText(strip=True)
    if not contains_number(artist_name_text):
        artist_names_list_for_user_picked_date.append(artist_name_text)

# Print the list of artist names
print("Artist Name:")
for artist_name in artist_names_list_for_user_picked_date:
    print(artist_name)
