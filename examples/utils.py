from nyaax.containers import Torrent


def print_torrent(torrent: Torrent) -> None:
    print("Title:       ", torrent.title)
    print("Category:    ", torrent.category)
    print("Subcategory: ", torrent.subcategory)
    print("Code:        ", torrent.code)
    print("Comments:    ", torrent.comments)
    print("Downloads:   ", torrent.completed_downloads)
    print("Seedes:      ", torrent.seeders)
    print("Leechers:    ", torrent.leechers)
    print("Date:        ", torrent.date)
    print("Info Hash:   ", torrent.info_hash)
    print("Size:        ", torrent.size)
    print("Submitter:   ", torrent.submitter)
    print("Type:        ", torrent.torrent_type)
    print("Magnet Link: ", torrent.magnet_link)
    print("Info:        ", torrent.information)
