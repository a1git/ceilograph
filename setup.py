#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ceilograph',
    version='1.0.0',
    description='A tool for publishing ceilometer metrics to graphite',
    author='Sashi Dahal',
    author_email='shashi.eu@gmail.com',
    url='https://github.com/a1git/ceilograph',
    install_requires=open('requirements.txt').readlines(),
    packages=find_packages(),
    entry_points = {
        'ceilometer.publisher': [
            'graphite=ceilograph.graphite:GraphitePublisher',
        ],
    }
)
