# setup.py - Setup script for packaging and installation

from setuptools import setup, find_packages

setup(
    name='file_copy_app',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # If your project requires any third-party libraries, list them here.
        # e.g., 'requests', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            'file_copy_app = file_copy_app.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
