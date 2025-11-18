import requests
import os
import _types
from typing import Callable, Union, List
import nyaax.extractors
from nyaax.containers import Torrent, Comment, View

_SAVE_RESPONSES = True
if _SAVE_RESPONSES:
    _SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'responses')
    os.makedirs(_SAVE_DIR, exist_ok=True)

_SESSION = requests.session()

_PARSERS = [
    "html.parser",
    "lxml",
    "html5lib"
]


def _get_response_content(url: str) -> Union[str, bytes]:
    response = _SESSION.get(url)
    response.raise_for_status()
    if _SAVE_RESPONSES:
        filename = f'{url[8:].replace('/', '_')}.html'
        filepath = os.path.join(_SAVE_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
    return response.content


_MULTIPLE_TORRENT = [
    _get_response_content(url) for url in [
        'https://nyaa.si',
        'https://nyaa.si/user/Nanako',
        'https://sukebei.nyaa.si',
        'https://sukebei.nyaa.si/user/superelmo',
    ]
]

_MULTIPLE_TORRENT_RSS = [
    _get_response_content(url) for url in [
        'https://nyaa.si/?page=rss',
        'https://nyaa.si/?q=Lain&s=comments&o=asc&page=rss',
    ]
]

_SINGLE_TORRENT = [
    _get_response_content(url) for url in [
        'https://nyaa.si/view/1852431',
        'https://nyaa.si/view/1852419',
        'https://nyaa.si/view/1852396',
    ]
]


def _inputs(contents: List[Union[str, bytes]]) -> Callable:
    def _decorator(func: Callable) -> Callable:
        def _inner() -> None:
            for content in contents:
                func(content)
        return _inner
    return _decorator


def _extractor(extractor_func_name: str) -> Callable:
    def _decorator(func: Callable) -> Callable:
        def _inner(content: Union[str, bytes]) -> None:
            for parser in _PARSERS:
                data = getattr(nyaax.extractors, extractor_func_name)(content, parser)
                func(data)
        return _inner
    return _decorator


@_inputs(_SINGLE_TORRENT)
@_extractor('get_single_torrent')
def test_single_torrent(data: Torrent) -> None:
    _types.check_torrent_fields(data)


@_inputs(_MULTIPLE_TORRENT)
@_extractor('get_multiple_torrents')
def test_multiple_torrent(data: List[Torrent]) -> None:
    _types.check_torrents_fields(data)


@_inputs(_MULTIPLE_TORRENT_RSS)
@_extractor('get_multiple_torrents_rss')
def test_multiple_torrent_rss(data: List[Torrent]) -> None:
    _types.check_torrents_fields(data)


@_inputs(_SINGLE_TORRENT)
@_extractor('get_comments')
def test_comments(data: List[Comment]) -> None:
    _types.check_comments_fields(data)


@_inputs(_SINGLE_TORRENT)
@_extractor('get_description')
def test_description(data: str) -> None:
    assert isinstance(data, str)


@_inputs(_SINGLE_TORRENT)
@_extractor('get_view')
def test_view(data: View) -> None:
    _types.check_view_fields(data)
