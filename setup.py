#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(
    name='BBpystepper',
    version='0.0.1',
    author='Pete Bachant',
    author_email='petebachant@gmail.com',
    py_modules=['bbpystepper'],
    scripts=[],
    url='https://github.com/petebachant/BBpystepper.git',
    license='LICENSE',
    description='Module for stepper motor control with the BeagleBone Black',
    long_description=open('README.md').read(),
)
