from __future__ import print_function
from setuptools import setup


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()
    return long_description


# Package meta-data.
NAME = "pantry_cloud"
DESCRIPTION = "A Python package implimenting getpantry.cloud usage."
KEYWORDS = [NAME, "JSON", "API", "CLOUD STORAGE"]
GIT_URL = "https://github.com/sarvesh4396/pantry-cloud"
AUTHOR = "Sarvesh Kumar Dwivedi"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.1.0"


setup(
    name=NAME,
    packages=[NAME],
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    url=GIT_URL,
    download_url="https://github.com/sarvesh4396/pantry-cloud/archive/refs/tags/V1.1.tar.gz",
    install_requires=["requests"],
    include_package_data=True,
    license="MIT",
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Communications :: File Sharing",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
