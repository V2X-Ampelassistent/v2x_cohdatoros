#!/usr/bin/env python3

import socket
import rclpy
import json
from rclpy.node import Node
from v2x_cohdainterfaces.msg import GPS
#from builtin_interfaces import builtin_interfaces__msg__Time__fini

class GPSPublisher(Node):

    def __init__(self):
        super().__init__('GPS_Publisher')
        self.publisher = self.create_publisher(GPS, 'Cohda_Signals', 10)
    
    def send_GPS(self, data):
        msg = GPS()
        # decode the Data to a string
        data_string = data.decode('utf-8')
        # split the string after each json (separated by "\r\n")
        data_list = data_string.split("\r\n")
        # read and send each json in msg 
        data_list.remove("")
        for json_string in data_list:
            data_json = json.loads(json_string)
            print(data_json)
           # try:
            if data_json["class"] == "TPV" and data_json["mode"] == 3:
                msg.classtype = data_json["class"]
                msg.device = data_json["device"]
                msg.mode = data_json["mode"]
                # msg.sendtime = data_json["time"]
                msg.ept = data_json["ept"]
                msg.lat = data_json["lat"]
                msg.lon = data_json["lon"]
                msg.alt = data_json["alt"]
                msg.epx = data_json["epx"]
                msg.epy = data_json["epy"]
                msg.epv = data_json["epv"]
                msg.track = data_json["track"]
                msg.speed = data_json["speed"]
                msg.climb = data_json["climb"]
                msg.eps = data_json["eps"]
                msg.epc = data_json["epc"]
                self.publisher.publish(msg)
                self.get_logger().info('Publishing: %s"' % data)
           # except:
           #     self.get_logger().info('Failed to send JSON. Probably wrong JSON format: %s"' % json_string)



def main(args=None):
    # Create socket for IPv6 UDP connection
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    # Bind any address to port 37010
    sock.bind(("::", 37010))
    rclpy.init(args=args)
    Publisher = GPSPublisher()
    # ingnore the very first transmit
    data, addr = sock.recvfrom(65507)
    while True:
        data, addr = sock.recvfrom(65507)
        print("received message: %s" % data)
        Publisher.send_GPS(data)

if __name__ == "__main__":
    main()