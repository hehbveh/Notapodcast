import requests

URL = "https://www.omnycontent.com/d/playlist/e73c998e-6e60-432f-8610-ae210140c5b1/0db4414e-bce3-43c7-a46c-b28900eb4ee3/6658c53e-d5b2-4ca8-8fa1-b28900eb4f04/podcast.rss"

old = "applepodcast@howstuffworks.com"
new = "hehbveh@gmail.com"

r = requests.get(URL)
r.raise_for_status()

xml = r.text.replace(old, new)

with open("omny.xml", "w", encoding="utf-8") as f:
    f.write(xml)
