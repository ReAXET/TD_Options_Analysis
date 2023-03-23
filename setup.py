"""Python setup.py for td_options_analysis package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("td_options_analysis", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="td_options_analysis",
    version=read("td_options_analysis", "VERSION"),
    description="Awesome td_options_analysis created by ReAXET",
    url="https://github.com/ReAXET/TD_Options_Analysis/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ReAXET",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["td_options_analysis = td_options_analysis.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
