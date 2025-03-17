from setuptools import setup, find_packages
import os
import sys
import platform

with open("README-base.md","r") as file:
    readme_content = file.read()

# Setup script
setup(
    name='lib3mf',
    version='2.4.1',
    description='lib3mf is an implementation of the 3D Manufacturing Format file standard',
    long_description=readme_content,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
