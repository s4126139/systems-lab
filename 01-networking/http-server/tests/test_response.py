from http_server.response import build_response


def test_response_starts_with_status_line():
    response = build_response(
        200,
        "OK",
        b"Hello",
        "test-request-id",
    )

    assert response.startswith(b"HTTP/1.1 200 OK\r\n")