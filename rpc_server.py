from xmlrpc.server import SimpleXMLRPCServer
import socket

def run_server(func):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        free_port = s.getsockname()[1]

    server = SimpleXMLRPCServer(("localhost", free_port))
    print(f"Listening on port {free_port}...")
    server.register_function(func, func.__name__)
    server.serve_forever()
