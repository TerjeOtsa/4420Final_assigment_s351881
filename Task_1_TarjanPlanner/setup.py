from setuptools import setup, find_packages

setup(
    name="TarjanPlanner",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "geopy",
        "networkx",
        "matplotlib",
    ],
    description="A Python package for planning optimized travel routes.",
    author="Terje Otterlei Saltskår",
    author_email="Terjeos00@gmail.com",
)
