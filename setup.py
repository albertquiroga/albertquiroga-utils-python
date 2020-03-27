from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='albertquiroga_utils',
    version='1.0.0',
    author="Albert Quiroga",
    author_email="albertquirogabertolin@gmail.com",
    description="Personal utilities for Python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albertquiroga/albertquiroga-utils-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Utilities"
    ],
    install_requires=['boto3'],
    python_requires='>=3.5'  # TODO check the minimum version
)
