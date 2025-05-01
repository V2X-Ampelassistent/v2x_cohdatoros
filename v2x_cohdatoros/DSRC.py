#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
import sys
from v2x_cohdainterfaces.msg import *
from .SPATEM import *
from .MAPEM import *
from .UDPService import *
import threading

class DSRCHandler(Node):
    def __init__(self):
        super().__init__('DSRC_Handler')
        self.declare_parameter('port', 37008)

        self.UDP = UDPService()
        # Create Publisher for each message format.
        self.SPATEMPub = SPATEMPublisher()
        self.MAPEMPub = MAPEMPublisher()

        # start background thread:
        thread = threading.Thread(target=self.listen_to_port)
        thread.daemon = True
        thread.start()

    def listen_to_port(self):
        while True:
            port = self.get_parameter('port').value
            self.UDP.connect_udp(port)
            while port == self.get_parameter('port').value:
                # receive and decode
                try:
                    data, type = self.UDP.resolve_udp_packets()
                    # Publish
                    if type == 'SPATEM':
                        self.SPATEMPub.send(data)
                    elif type == 'MAPEM':
                        self.MAPEMPub.send(data)
                except socket.timeout:
                    self.get_logger().info("Listening on Port %i. No Data received." % port)
                    continue
                except Exception as error:
                    if error == KeyboardInterrupt:
                        sys.exit()
                    else:
                        self.get_logger().info(str(error))
                    pass
            # disconnect, if a new port has been set.
            self.UDP.disconnect_udp()

def main(args=None):
    rclpy.init(args=args)
    Handler = DSRCHandler()
    # start the threads:
    executor = MultiThreadedExecutor()
    executor.add_node(Handler)
    executor.add_node(Handler.MAPEMPub)
    executor.add_node(Handler.SPATEMPub)
    executor.spin()
    # clean up
    rclpy.shutdown()

if __name__ == "__main__":
    main()