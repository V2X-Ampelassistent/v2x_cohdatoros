#!/usr/bin/env python3

import rclpy
import sys
from v2x_cohdainterfaces.msg import *
from .SPATEM import *
from .MAPEM import *
from .UDPService import *

def main(args=None):
    UDP = UDPService()
    rclpy.init(args=args)
    # Create Publisher for each message format.
    SPATEMPub = SPATEMPublisher()
    MAPEMPub = MAPEMPublisher()

    while True:
        # receive and decode
        try:
            data, type = UDP.resolve_udp_packets()
        except Exception as error:
            if error == KeyboardInterrupt:
                sys.exit()
            else:
                print(error)
            pass
        # Publish
        if type == 'SPATEM':
            SPATEMPub.send(data)
        elif type == 'MAPEM':
            MAPEMPub.send(data)

if __name__ == "__main__":
    main()