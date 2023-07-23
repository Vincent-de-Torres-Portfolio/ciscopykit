from setuptools import setup, find_packages

setup(
    name='ciscopykit',
    version='2.1.3',
    author='devinci-it',
    author_email='vince.dev@icloud.com',
    description='A network management toolkit for Cisco devices keeping track of devices when using GNS3 / Cisco Packet Tracer',
    long_description='''A network management toolkit for Cisco devices. It provides classes and methods to manage network devices, interfaces, and configurations.''',
    url='https://github.com/Vincent-de-Torres-Portfolio/ciscopykit',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11'



    ],
    install_requires=[
        'click',
        'networkx',
        'matplotlib',
        'ipaddress',
        'argparse'
    ],
    entry_points={
        'console_scripts': [
            'ciscopykit = ciscopykit.entry_point:main',
            'switch = ciscopykit.switch.app:main',
            'services=ciscopykit.services.app:main',
            'vlan=ciscopykit.vlan.app:main',
            'lan_security = ciscopykit.lan_security.app:main'
        ],
    },
)
