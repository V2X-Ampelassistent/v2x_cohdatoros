#!/usr/bin/env python3

import socket
import rclpy
import json
from rclpy.node import Node
from v2x_cohdainterfaces.msg import GPS
import threading
from sensor_msgs.msg import NavSatFix

class GPSPublisher(Node):

    def __init__(self):
        super().__init__('GPS_Publisher')
        self.declare_parameter('port', 37010)
        self.publisher = self.create_publisher(GPS, 'Cohda_Signals/GPS', 10)

        # start background thread:
        thread = threading.Thread(target=self.listen_to_port)
        thread.daemon = True
        thread.start()
    
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
            if data_json["class"] == "TPV" and data_json["mode"] == 3:
                msg.classtype = data_json.get("class")
                msg.device = data_json.get("device")
                msg.mode = data_json.get("mode")
                msg.ept = data_json.get("ept")
                msg.lat = data_json.get("lat")
                msg.lon = data_json.get("lon")
                msg.alt = data_json.get("alt")
                msg.epx = data_json.get("epx")
                msg.epy = data_json.get("epy")
                msg.epv = data_json.get("epv")
                msg.track = data_json.get("track")
                msg.speed = data_json.get("speed")
                msg.climb = data_json.get("climb")
                msg.eps = data_json.get("eps")
                msg.epc = data_json.get("epc")

                self.publisher.publish(msg)
                self.get_logger().info('Publishing: %s"' % data)
            else:
                self.get_logger().info('received GPS in unsupported Mode. No GPS Message published.')

    def listen_to_port(self):
        while rclpy.ok():
            # Get Parameters from ROS Node
            port = self.get_parameter('port').value
            self.get_logger().info('Listening for GPS Data on Port %i!' % port)
            # Create socket for IPv6 UDP connection
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            # Bind any address to port 37010
            sock.bind(("::", port))
            # set a timeout
            sock.settimeout(10.0)
            while self.get_parameter('port').value == port:
                try:
                    data, addr = sock.recvfrom(65507)
                    self.send_GPS(data)
                except socket.timeout:
                    self.get_logger().info("Listening on Port %i. No Data received." % port)
                    continue
            sock.close()



def main(args=None):
    rclpy.init(args=args)
    Publisher = GPSPublisher()
    rclpy.spin(Publisher)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
