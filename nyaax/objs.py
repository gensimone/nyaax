from datetime import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass(unsafe_hash=True)
class User:
    name: str
    trusted: bool


@dataclass(unsafe_hash=True)
class Torrent:
    size: int
    date: datetime
    seeders: int
    leechers: int
    completed_downloads: int
    category: str
    subcategory: str
    title: str
    code: int
    magnet_link: str
    comments: int = 0
    torrent_type: Optional[str] = None
    information: Optional[str] = None
    info_hash: Optional[str] = None
    submitter: Optional[User] = None


@dataclass(unsafe_hash=True)
class Comment:
    user: User
    date: str
    text: str
    avatar: Optional[str]


@dataclass(unsafe_hash=True)
class View:
    torrent: Torrent
    description: str
    comments: list[Comment]
