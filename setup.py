from setuptools import find_packages, setup

setup(
    # Application name:
    name="eventique",
    # Version number (initial):
    version=open("./VERSION").read(),
    # Application author details:
    author="MAJDOUB Khalid",
    author_email="majdoub.khalid@gmail.com",
    # Packages
    packages=find_packages(),
    # Include additional files into the package
    include_package_data=True,
    # Details
    url="https://github.com/hadamrd/eventique",
    #
    # license="LICENSE.txt",
    description="Light and standalone python events manager.",
    long_description=open("README.md").read(),
    # Dependent packages (distributions)
    install_requires=open("./requirements.txt").readlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ]
)
