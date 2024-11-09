from setuptools import setup

package_name = 'v2x_cohdatoros'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/resource', ["resource/DSRC.asn", 
             "resource/ETSI-ITS-CDD.asn",
             "resource/MAPEM-PDU-Descriptions.asn", 
             "resource/SPATEM-PDU-Descriptions.asn"]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zdm',
    maintainer_email='todo@todo.de',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'GPS_publisher = v2x_cohdatoros.GPS:main',
            'DSRC_publisher = v2x_cohdatoros.DSRC:main',
        ],
    },
)
