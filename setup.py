import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup

setup(
    name='micropython-pcd8544',
    py_modules=['pcd8544'],
    version='1.1.0',
    description='MicroPython library for the PCD8544 LCD, used by Nokia 5110 displays.',
    long_description='This library lets you communicate with LCDs using the Philips PCD8544 84x48 monochrome LCD driver, for example the Nokia 5110 display.',
    keywords='pcd8544 monochrome lcd nokia micropython',
    url='https://github.com/mcauser/micropython-pcd8544',
    author='Mike Causer',
    author_email='mcauser@gmail.com',
    maintainer='Mike Causer',
    maintainer_email='mcauser@gmail.com',
    license='MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: OSI Approved :: MIT License',
    ],
)