from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="browser-cat",
    version="0.1.0",
    scripts=['bcat'],

    # metadata to display on PyPI
    author="Dhananjay Balan",
    author_email="mail@dbalan.in",
    description="Cat to browser",
    license="BSD",
    keywords="text mua mutt browser cat",
    url="http://github.com/dbalan/browser-cat",
    project_urls={
        "Bug Tracker": "http://github.com/dbalan/browser-cat/issues",
        "Documentation": "http://github.com/dbalan/browser-cat",
        "Source Code": "http://github.com/dbalan/browser-cat",
    }
    long_description=long_description,
)
