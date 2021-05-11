import socket


class NotConnectedError(Exception):
    """Exception to alert the user to incorrect use of the Client class."""
    def __init__(self):
        """Initialize class instance."""
        super().__init__("Don't expect a message from the server if you're not connected to it.")


class Client:
    """A client of a single server.TcpServer.

    Attributes:
        ip: IP-address of the server this client is associated with.
        port: port of the server this client is associated with.
        main_socket: socket.socket object belonging to this client.
        connected: true if connected to the associated server, false if not."""
    def __init__(self, ip: str, port: int):
        """Initialize class instance.

        Args:
            ip: IP-address of the server to connect to.
            port: port of the server to connect to."""
        self.ip = ip
        self.port = port
        self.main_socket = socket.socket()
        self.connected = False

    def connect(self):
        """Establish a connection to the server associated with this client."""
        self.main_socket.connect((self.ip, self.port))
        self.connected = True

    def disconnect(self):
        """Disconnect from the server associated with this client."""
        self.connected = False
        self.main_socket.close()

    def wait_for_message(self) -> str: #TODO: Check wether typehint is actually correct
        """Wait to recieve a single message from the server associated with this client.

        Returns:
            the first message recieved from the server, decoded.

        Raises:
            NotConnectedError: not connected to the server."""
        if not self.connected:
            raise NotConnectedError
        return self.main_socket.recv(4096).decode()

