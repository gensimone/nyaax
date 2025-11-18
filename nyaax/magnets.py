from urllib.parse import urlencode, quote


_KNOWN_TRACKERS = [
    "http://nyaa.tracker.wf:7777/announce",
    "udp://open.stealth.si:80/announce",
    "udp://tracker.opentrackr.org:1337/announce",
    "udp://exodus.desync.com:6969/announce",
    "udp://tracker.torrent.eu.org:451/announce",
]


def magnet_builder(info_hash: str, title: str) -> str:
    magnet_link = (
        f"magnet:?xt=urn:btih:{info_hash}&"
        + urlencode({"dn": title}, quote_via=quote)
    )
    for tracker in _KNOWN_TRACKERS:
        magnet_link += f"&{urlencode({'tr': tracker})}"
    return magnet_link
