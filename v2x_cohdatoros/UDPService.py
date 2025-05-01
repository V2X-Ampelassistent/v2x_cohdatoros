import socket
import asn1tools
from ament_index_python.packages import get_package_share_directory

class UDPService():
    def __init__(self):
        package_share_directory = get_package_share_directory('v2x_cohdatoros')
        self.asnspec = asn1tools.compile_files(
            [package_share_directory + "/resource/DSRC.asn", 
             package_share_directory + "/resource/ETSI-ITS-CDD.asn",
             package_share_directory + "/resource/MAPEM-PDU-Descriptions.asn", 
             package_share_directory + "/resource/SPATEM-PDU-Descriptions.asn"], 'uper')
        # Uncomment the following line for Overview of possible structure:
        # print(self.asnspec.modules['ETSI-ITS-DSRC']['SPAT'])

    def connect_udp(self, port):
        # Create socket for IPv6 UDP connection
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind any address to given port
        self.sock.bind(("0.0.0.0", port))
        # set a timeout
        self.sock.settimeout(10.0)

    def disconnect_udp(self):
        self.sock.close()

    def _handle_mapem(self, data):
        decoded = False
         # Use asn sequence 'MAPEM' with asn1tools to decode the bytestring after the MAPEM identifier
        decoded = self.asnspec.decode(
            'MAPEM', data[data.index(b'\x02\x05\x00'):])

        if decoded:
            return decoded, 'MAPEM'

    def _handle_spatem(self, data):
        decoded = False
        # Use asn sequence 'SPATEM' with asn1tools to decode the bytestring after the SPATEM identifier
        decoded = self.asnspec.decode(
            'SPATEM', data[data.index(b'\x02\x04\x00'):])

        if decoded:
            return decoded, 'SPATEM'

    def resolve_udp_packets(self):
        data, addr = self.sock.recvfrom(4096)
        if b'\x02\x05\x00' in data:
            return self._handle_mapem(data)
        if b'\x02\x04\x00' in data:
            return self._handle_spatem(data)

        return False, False