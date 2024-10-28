#!/usr/bin/env python3

import socket
import rclpy
import asn1tools
import sys
from rclpy.node import Node
from v2x_cohdainterfaces.msg import MAPEM, SPATEM

class DSRCPublisher(Node):

    def __init__(self):
        super().__init__('DSRC_Publisher')
        self.MapemPublisher = self.create_publisher(MAPEM, 'Cohda_Signals/MAPEM', 10)
        self.SpatemPublisher = self.create_publisher(SPATEM, 'Cohda_Signals/SPATEM', 10)
    
    def send(self, data, type):
        if type == 'MAPEM':
            msg = MAPEM()
            msg.mapem = str(data)
            self.MapemPublisher.publish(msg)
            self.get_logger().info('Published MAPEM')
            return
        elif type == 'SPATEM':
            msg = SPATEM()
            msg.spatem = str(data)
            self.SpatemPublisher.publish(msg)
            self.get_logger().info('Published SPATEM')
            return
        self.get_logger().info('Nothing to Publish.')


class UDPService():
    def __init__(self):
        # Create socket for IPv6 UDP connection
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Bind any address to port 37008
        self.sock.bind(("0.0.0.0", 37008))

        self.asnspec = asn1tools.compile_files("/home/zdm/ampelassistent/ROS_ws/src/v2x_cohdatoros/resource/etsi_mapem_spatem.asn", 'uper')

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

def main(args=None):
    UDP = UDPService()
    rclpy.init(args=args)
    Pub = DSRCPublisher()
    i = 0
    while True:
        try:
            data, type = UDP.resolve_udp_packets()
        except Exception as error:
            if error == KeyboardInterrupt:
                sys.exit()
            else:
                print(error)
            pass
        Pub.send(data, type)

if __name__ == "__main__":
    main()