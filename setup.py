from setuptools import setup, find_packages
setup(
    name="browser-cat",
    version="0.1.0",
    scripts=['bcat'],

    # metadata to display on PyPI
    author="Dhananjay Balan",
    author_email="mail@dbalan.in",
    description="Cat to browser",
    license="BSD",
    keywords="mutt browser cat",
    url="http://github.com/dbalan/browser-cat",   # project home page, if any
    project_urls={
        "Bug Tracker": "http://github.com/dbalan/browser-cat/issues",
        "Documentation": "http://github.com/dbalan/browser-cat",
        "Source Code": "http://github.com/dbalan/browser-cat",
    }

    # could also include long_description, download_url, classifiers, etc.
)
