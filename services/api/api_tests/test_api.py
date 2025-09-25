from http import HTTPStatus

from api.manager import TinyKrakenAPIManager
from aws_lambda_powertools.event_handler import content_types


def test_list_comments(monkeypatch, tiny_kraken_entries):
    manager = TinyKrakenAPIManager()
    monkeypatch.setattr(manager.model, "list_comments", lambda: tiny_kraken_entries)
    response = manager.list_comments()

    assert response.status_code == HTTPStatus.OK
    assert response.content_type == content_types.APPLICATION_JSON


def test_list_comments_not_found(monkeypatch):
    manager = TinyKrakenAPIManager()
    monkeypatch.setattr(manager.model, "list_comments", lambda: [])
    response = manager.list_comments()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.content_type == content_types.APPLICATION_JSON


def test_get_comment(monkeypatch, tiny_kraken_entry):
    manager = TinyKrakenAPIManager()
    monkeypatch.setattr(manager.model, "get_comment", lambda x: tiny_kraken_entry)
    response = manager.get_comment(tiny_kraken_entry.comment_id)

    assert response.status_code == HTTPStatus.OK
    assert response.content_type == content_types.APPLICATION_JSON


def test_get_comment_not_found(monkeypatch):
    manager = TinyKrakenAPIManager()
    monkeypatch.setattr(manager.model, "get_comment", lambda x: None)
    response = manager.get_comment("comment_id_5")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.content_type == content_types.APPLICATION_JSON
