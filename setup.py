import json
from setuptools import setup, find_packages # type:ignore

with open("data.json", "r", encoding="utf-8") as f: version: str = json.load(f)["version"]

setup(
    author="AJ-Holzer",
    description="A simple module which does some simple stuff. Don't make something illegal ;)",
    url="https://github.com/AJ-Holzer/AJ-Module",
    license="MIT",
    name='ajpack',
    version=version,
    packages=find_packages(),
    install_requires=[
        "pyzipper",
        "opencv-python",
        "requests",
        "Pillow",
        "keyboard",
        "pywin32",
        "psutil",
        "winshell",
        "plyer",
        "customtkinter"
    ],
    entry_points={
        'console_scripts': [
            # Commands
        ],
    },
)