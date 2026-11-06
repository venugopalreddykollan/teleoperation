from glob import glob
import os

from setuptools import setup


package_name = 'telop'

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            [os.path.join('resource', package_name)],
        ),
        (os.path.join('share', package_name), ['package.xml']),
        (
            os.path.join('share', package_name, 'description'),
            glob('description/*'),
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py'),
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='UR5e teleoperation and visualization package',
    maintainer='venugopal reddy kollan',
    maintainer_email='venugopal.reddy.kollan@gmail.com',
    license='Apache-2.0',
)