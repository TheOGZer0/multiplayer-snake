import socket


class DestinationError(Exception):
    """Exception to alert user to the fact they're trying to send data
    to an address that isn't currently connected to the server."""
    def __init__(self, address: str):
        """Initialize class instance.

        Args:
            address: the faulty address."""
        super().__init__(f"Address {address} not a known open connection for server.")


class TcpServer:
    """TcpServer used for network-unintensive multiplayer gaming
    that allows for multiple client to be connected at the same time.

    Attributes:
        port: the server's port.
        main_socket: the main/initial socket.socket object belonging to the server.
        connections: dictionairy containing connected addresses as keys,
            and a corresponding socket.socket object as value.
            NOTE: Clients that have unexpectedly disconnected will still be in here."""
    def __init__(self, port: int):
        """Initialize class instance, bind to port.

        Args:
            port: the port the server should run at."""
        self.port = port
        self.main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.main_socket.bind(('', port))
        self.connections = {}

    def listen_for_connections(self, connection_limit: int = 999): #TODO: Implement another stop condition
        """Listen for clients trying to connect, wait until a certain amount of clients has connected.
        Assign connections to self.connections.

        Args:
            connection_limit: amount of clients that are expected to connect.
        """
        self.main_socket.listen(5)
        while True:
            c_socket, address = self.main_socket.accept()
            self.connections[address] = c_socket
            if len(self.connections) >= connection_limit:
                break

    def send(self, address: str, content):
        """Send something to a connected client at a certain address.

        Args:
            address: the client's address.
            content: whatever should be sent (datatypes except string are untested so far).

        Raises:
            DestinationError: attempted to send something to unknown/unconnected address."""
        if address in self.connections: #Performance could be improved by not checking this for sendall()
            self.connections[address].send(content.encode())
        else:
            raise DestinationError(address)

    def send_all(self, content):
        """Send something to all connected clients.

        Args:
            content: whatever should be sent."""
        for address in self.connections.keys():
            self.send(address, content)
