#The minimal structure of HTTP response
# HTTP/1.1 200 OK
# Content-Type: text/plain; charset=utf-8
# Content-Length: 5
# Connection: close

# Hello
# HTTP/1.1 200 OK\r\n -status line
# Content-Type: text/plain; charset=utf-8\r\n -header
# Content-Length: 5\r\n -header
# Connection: close\r\n -header
# \r\n
# Hello -body

def build_response(
    status_code: int,
    reason: str,
    body: bytes,
    request_id: str,
    )-> bytes:
    # status_line = b"HTTP/1.1 200 OK\r\n" #b create bytes which socket sendall() need bytes, so response seralizer must return bytes

    status_line = (
        f"HTTP/1.1 {status_code} {reason}\r\n".encode("ascii")
    )

    content_type_header = (
        b"Content-Type: text/plain; charset=utf-8\r\n"
    )

    content_length_header = (
        f"Content-Length: {len(body)}\r\n".encode("ascii")
    )

    request_id_header = (
    f"X-Request-Id: {request_id}\r\n".encode("ascii")
    )

    connection_header = b"Connection: close\r\n"

    blank_line = b"\r\n"

    return (
        status_line
        + content_type_header
        + content_length_header
        + request_id_header
        + connection_header
        + blank_line
        + body
    )

