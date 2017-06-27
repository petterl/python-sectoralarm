""" Setup for python-sectoralarm """

from setuptools import setup

setup(
    name='sectoralarm',
    version='1.0.0',
    description='Read and change status of sector alarm devices through api.',
    long_description='A module for reading and changing status of ' +
    'sectoralarm devices through App API. Compatible ' +
    'with both Python2.7 and Python3.',
    url='http://github.com/petterl/python-sectoralarm',
    author='Petter Sandholdt',
    author_email='petter@sandholdt.se',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='home automation sectoralarm',
    install_requires=['requests>=2.9.1'],
    packages=['sectoralarm'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'sectoralarm=sectoralarm.__main__:main',
        ]
    })
