import requests
from examples.utils import print_torrent
from nyaax.extractors import get_view


url = "https://nyaa.si/view/2044284"

response = requests.get(url)
response.raise_for_status()

view = get_view(response.content, "lxml")

torrent = view.torrent
description = view.description
comments = view.comments

print_torrent(torrent)
print("Description: ", description)
print("Comments: ")
for comment in view.comments:
    print(view.comments)
