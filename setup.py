from setuptools import setup, find_packages
from pathlib import Path


long_description = Path("README.md").read_text() if Path("README.md").exists() else ""


setup(
    name="dwd_downloader",
    version="0.1.0",
    author="Aranil",
    author_email="linara.arslanova@uni-jena.de",
    description="This module is a customized extension of dbflow, designed to automate downloading DWD (Deutscher Wetterdienst) data from the FTP server and store it in an SQLite database. It leverages web scraping technique.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aranil/dwd_downloader",
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
    package_data={
        'dwd_downloader': ['sql/*.sql'],  # Include all .sql files in the sql folder
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.10',
    install_requires=[
        "dbflow @ git+ssh://git@github.com/Aranil/dbflow.git@main"
    ],
)

# run to generate a python package
# python setup.py sdist bdist_wheel

# run to install required packages in conda env
# conda env create -f environment.yml

# run to install package
# pip install git+ssh://git@github.com/your-user/your-private-repo.git

# TODO: tests, logfiles!!!
