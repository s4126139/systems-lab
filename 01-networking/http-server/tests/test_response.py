from http_server.response import build_response


def test_response_starts_with_status_line():
    response = build_response(
        200,
        "OK",
        b"Hello",
        "test-request-id",
    )

    assert response.startswith(b"HTTP/1.1 200 OK\r\n")

def test_response_calculates_content_length_from_body_bytes():
    body = "é".encode("utf-8")

    response = build_response(
        200,
        "OK",
        body,
        "test-request-id",
    )

    assert b"Content-Length: 2\r\n" in response

def test_response_separates_headers_and_body():
    body = b"Hello"

    response = build_response(
        200,
        "OK",
        body,
        "test-request-id",
    )

    headers, separator, response_body = response.partition(
        b"\r\n\r\n"
    )

    assert separator == b"\r\n\r\n"
    assert response_body == body

def test_response_contains_request_id_header():
    request_id = "abc123"

    response = build_response(
        200,
        "OK",
        b"Hello",
        request_id,
    )

    headers, separator, body = response.partition(b"\r\n\r\n")

    assert separator == b"\r\n\r\n"
    assert b"X-Request-Id: abc123\r\n" in headers

def test_response_uses_provided_status():
    response = build_response(
        404,
        "Not Found",
        b"Not Found",
        "test-request-id",
    )

    assert response.startswith(
        b"HTTP/1.1 404 Not Found\r\n"
    )