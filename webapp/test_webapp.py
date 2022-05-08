from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_info():
    response = client.get("/info")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"Receiver": "Cisco is the best!"}


def test_ping():
    response = client.post(
        "/ping",
        json={"url": "https://raw.githubusercontent.com/torvalds/linux/master/README"},
    )
    expected = {
        "response": """Linux kernel
============

There are several guides for kernel developers and users. These guides can
be rendered in a number of formats, like HTML and PDF. Please read
Documentation/admin-guide/README.rst first.

In order to build the documentation, use ``make htmldocs`` or
``make pdfdocs``.  The formatted documentation can also be read online at:

    https://www.kernel.org/doc/html/latest/

There are various text files in the Documentation/ subdirectory,
several of them using the Restructured Text markup notation.

Please read the Documentation/process/changes.rst file, as it contains the
requirements for building and running the kernel, and information about
the problems which may result by upgrading your kernel.
"""
    }
    assert response.json() == expected


def test_invalid_certificate():
    """Test that/ping endpoint handles invalid ssl certificates."""
    body = {"url": "https://expired.badssl.com"}
    response = client.post("/ping", json=body)

    expected = {
        "response": """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="/icons/favicon-red.ico"/>
  <link rel="apple-touch-icon" href="/icons/icon-red.png"/>
  <title>expired.badssl.com</title>
  <link rel="stylesheet" href="/style.css">
  <style>body { background: red; }</style>
</head>
<body>
<div id="content">
  <h1 style="font-size: 12vw;">
    expired.<br>badssl.com
  </h1>
</div>

</body>
</html>
"""
    }
    assert response.json() == expected


@pytest.mark.parametrize(
    "body, error_type",
    (
        ({"not_an_url": "zażółcił gęślą jaźń 🦆🐱‍👤 🏢🖥"}, "value_error.missing"),
        ({"url": "zażółcił gęślą jaźń 🦆🐱‍👤 🏢🖥"}, "value_error.url.scheme"),
    ),
)
def test_invalid_request(body, error_type):
    response = client.post("/ping", json=body)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["loc"] == ["body", "url"]
    assert response.json()["detail"][0]["type"] == error_type


def test_connection_error():
    body = {"url": "http://255.255.255.255:5336"}
    response = client.post("/ping", json=body)
    assert response.status_code == HTTPStatus.BAD_REQUEST
