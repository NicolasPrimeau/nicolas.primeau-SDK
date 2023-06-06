import pathlib

import setuptools
from setuptools import setup

_SCRIPT_PATH = pathlib.Path("./scripts")
setup(
    name='TheOneApiSDK',
    author="Nicolas.Primeau",
    author_email="nicolas.primeau@gmail.com",
    description="Description",
    version='1.0',
    python_requires=">=3.10.0",
    install_requires=[
        'requests>=2.31.0',
    ],
    packages=setuptools.find_packages(where="./src"),
    package_dir={'the_one_api_sdk': 'src/the_one_api_sdk'},
    entry_points={
        'console_scripts': [
            'the-one-api-sdk = the_one_api_sdk.cli.cli_client:main'
        ]
    },
)
