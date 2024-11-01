import socket
import asn1tools

class UDPService():
    def __init__(self):
        # Create socket for IPv6 UDP connection
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind any address to port 37008
        self.sock.bind(("0.0.0.0", 37008))

        self.asnspec = asn1tools.compile_files(
            ["/home/zdm/ampelassistent/ROS_ws/src/v2x_cohdatoros/resource/DSRC.asn", 
             "/home/zdm/ampelassistent/ROS_ws/src/v2x_cohdatoros/resource/ETSI-ITS-CDD.asn",
             "/home/zdm/ampelassistent/ROS_ws/src/v2x_cohdatoros/resource/MAPEM-PDU-Descriptions.asn", 
             "/home/zdm/ampelassistent/ROS_ws/src/v2x_cohdatoros/resource/SPATEM-PDU-Descriptions.asn"], 'uper')
        # Uncomment the following line for Overview of possible structure:
        # print(self.asnspec.modules['ETSI-ITS-DSRC']['SPAT'])

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