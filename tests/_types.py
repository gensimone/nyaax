from datetime import datetime
from nyaax.objs import Torrent, User, Comment, View


def check_torrent_fields(torrent: Torrent) -> None:
    assert isinstance(torrent, Torrent)

    assert isinstance(torrent.seeders, int)
    assert torrent.seeders >= 0

    assert isinstance(torrent.leechers, int)
    assert torrent.leechers >= 0

    assert isinstance(torrent.completed_downloads, int)
    assert torrent.completed_downloads >= 0

    assert isinstance(torrent.comments, int)
    assert torrent.comments >= 0

    assert isinstance(torrent.code, int)
    assert len(str(torrent.code)) == 7

    assert isinstance(torrent.title, str)
    assert isinstance(torrent.size, int)
    assert isinstance(torrent.date, datetime)
    assert isinstance(torrent.magnet_link, str)

    assert isinstance(torrent.category, str)
    assert isinstance(torrent.subcategory, str)

    if torrent.info_hash:
        assert isinstance(torrent.info_hash, str)
    if torrent.information:
        assert isinstance(torrent.information, str)
    if torrent.torrent_type:
        assert isinstance(torrent.torrent_type, str)
    if torrent.submitter:
        check_user_fields(torrent.submitter)


def check_torrents_fields(torrents: list[Torrent]) -> None:
    for torrent in torrents:
        check_torrent_fields(torrent)


def check_user_fields(user: User) -> None:
    assert isinstance(user, User)
    assert isinstance(user.name, str)
    assert isinstance(user.trusted, bool)


def check_comment_fields(comment: Comment) -> None:
    assert isinstance(comment, Comment)
    assert isinstance(comment.date, str)
    assert isinstance(comment.text, str)
    check_user_fields(comment.user)


def check_comments_fields(comments: list[Comment]) -> None:
    for comment in comments:
        check_comment_fields(comment)


def check_view_fields(view: View) -> None:
    assert isinstance(view, View)
    assert isinstance(view.description, str)
    check_torrent_fields(view.torrent)
    check_comments_fields(view.comments)
