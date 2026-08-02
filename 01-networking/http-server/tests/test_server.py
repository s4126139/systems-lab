from unittest.mock import MagicMock, patch

import pytest

from http_server.server import serve


def _run_one_request(request_bytes: bytes) -> bytes:
    server_socket = MagicMock()
    client_socket = MagicMock()

    server_socket.__enter__.return_value = server_socket

    server_socket.getsockname.return_value = (
        "127.0.0.1",
        4221,
    )

    server_socket.accept.side_effect = [
        (client_socket, ("127.0.0.1", 50000)),
        KeyboardInterrupt,
    ]

    client_socket.recv.return_value = request_bytes

    with patch(
        "http_server.server.socket.socket",
        return_value=server_socket,
    ):
        with pytest.raises(KeyboardInterrupt):
            serve()

    return client_socket.sendall.call_args.args[0]

def test_root_route_returns_hello():
    response = _run_one_request(
        b"GET / HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"\r\n"
    )

    assert response.startswith(b"HTTP/1.1 200 OK\r\n")
    assert response.endswith(b"\r\n\r\nHello")

def test_unknown_route_returns_not_found():
    response = _run_one_request(
        b"GET /missing HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"\r\n"
    )

    assert response.startswith(
        b"HTTP/1.1 404 Not Found\r\n"
    )
    assert response.endswith(
        b"\r\n\r\nNot Found"
    )

def test_malformed_request_line_returns_bad_request():
    response = _run_one_request(
        b"GET /\r\n"
        b"Host: localhost\r\n"
        b"\r\n"
    )

    assert response.startswith(
        b"HTTP/1.1 400 Bad Request\r\n"
    )
    assert response.endswith(
        b"\r\n\r\nBad Request"
    )

def test_non_ascii_request_line_returns_bad_request():
    response = _run_one_request(
        b"GET /\xff HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"\r\n"
    )

    assert response.startswith(
        b"HTTP/1.1 400 Bad Request\r\n"
    )
    assert response.endswith(
        b"\r\n\r\nBad Request"
    )

def test_health_route_returns_ok():
    response = _run_one_request(
        b"GET /health HTTP/1.1\r\n"
        b"Host: localhost\r\n"
        b"\r\n"
    )

    assert response.startswith(
        b"HTTP/1.1 200 OK\r\n"
    )
    assert response.endswith(
        b"\r\n\r\nOK"
    )