import socket

HOST = "127.0.0.1" #Localhost IP address
PORT = 4221 #Port of the running service
BUFFER_SIZE = 4096 # Maximum number of bytes requested from one recv() call

def serve():
    #socket.AF_INET said that socket uses IPv4 address
    #socket.SOCK_STREAM said that socket uses TCP stream
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT)) 
        #bind() requires operating system linked socket to host and port. 
        #Mental model: socket() -> create a phone, bind() -> provide phone number to the phone
        #before bind(): socket existed but didn't have the address
        #after bind(): socket blongs to 127.0.0.1:4221
        #bind() requires an address object - tuple(host, port)
        print(f"Bound to {server_socket.getsockname()}") #getsockname() asks Operating system bound which address?

        server_socket.listen() #listen() turn socket which had address to socket which is waiting the incoming TCP connections
        print(f"Listening on {server_socket.getsockname()}")

        while True:
            client_socket, client_address = server_socket.accept() #accept() is for waiting incoming connection
            #This is blocking operation: 
            # if no client:-> the program stands at accept(), not end, not lag
            # when a client connects, the accept() returns 2 values: client_socket and client_address
            # client_socket: this is the socket already used to communicate with the new connected client.
            # client_address: ex: ('127.0.0.1', 52741) - IP address of client and temporary client port do operating system selected
            #Client: 127.0.0.1:52741
            #            |
            #            | TCP connection
            #            |
            # Server: 127.0.0.1:4221

            with client_socket:  #each client connection has a different socket
                print(f"Connected by {client_address}") #when finish this block, client socket closes

                request_bytes = client_socket.recv(BUFFER_SIZE) #recv()- read the maximum of BUFFER_SIZE bytes of this client connection
                print(f"Received {len(request_bytes)} bytes")
                print(repr(request_bytes))
                # repr() prints the raw technical representation of the bytes object.
                # Useful for debugging because it reveals:
                # - escape characters like \r\n
                # - binary data
                # - exact byte values
                # Using print(request_bytes) may hide special characters,
                # but repr() shows the true underlying data.
if __name__=="__main__":
    serve()