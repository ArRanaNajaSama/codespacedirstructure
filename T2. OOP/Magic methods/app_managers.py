# Application Managers


from app_abstractions import ABCConnectionManager
from connections import SSH

class ConnectionManager(ABCConnectionManager):
    # ABCConnection.__subclasses__() can be used for product types

    def __new__(cls, *args, **kwargs):
        if len(cls.get_network_interfaces())<1:
            raise ConnectionError('Network interfaces not found!')
        else:
            return super().__new__(cls)

    def create_ssh(self, ip, *args, **kwargs):
        """Create ssh connection objects. Multiple sessions supported"""
        ssh = SSH(ip, *args, **kwargs)
        self.connections.setdefault(ssh, 'ssh connection')
        return ssh

    def create_ftp(self, *args, **kwargs):
        # create ftp connection
        pass

    def create_serial(self, *args, **kwargs):
        # create serial connection. Multiple session are not supported
        pass

    def create_telnet(self, *args, **kwargs):
        # create telnet connection
        pass

    def __len__(self):
        # len(dict.keys()) for simple dict
        return self.connections

    @classmethod
    def get_network_interfaces(cls):
        return ['wlan', 'modem']

if __name__ == "__main__":
    connections = ConnectionManager()
    ssh1 = connections.create_ssh('10.124.198.24')
    ssh2 = connections.create_ssh('10.124.106.29')
    for connection in connections.connections:
        print(f"Known connection {connection}")
    print(len(connections.connections))
