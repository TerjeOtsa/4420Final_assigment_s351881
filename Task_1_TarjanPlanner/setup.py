from setuptools import setup, find_packages

setup(
    name="TarjanPlanner",
    version="1.0.1",
    packages=find_packages(include=["TarjanPlanner", "TarjanPlanner.*"]),
    install_requires=[
        "geopy>=2.2.0",
        "networkx>=3.0",
        "matplotlib>=3.7.2",
        "pytest>=7.4.0",
        "prettytable>=3.6.0",
        "colorama>=0.4.6",
        "numpy>=1.26.0",
        "pandas>=2.1.0",
        "scipy>=1.11.3",
    ],
    extras_require={
        "dev": [
            "pytest-cov",
            "black",
            "flake8",
        ]
    },
    description="A Python package for planning optimized travel routes with visualization and automation.",
    long_description=open("TASK_1_TARJANPLANNER_README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TerjeOtsa/4420Final_assigment_s351881",
    author="Terje Otterlei Saltskår",
    author_email="Terjeos00@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "tarjanplanner=TarjanPlanner.main:main",
        ],
    },
    package_data={
        "TarjanPlanner": ["data/*"],  # Include all files in the 'data' directory
    },
    include_package_data=True,
)
