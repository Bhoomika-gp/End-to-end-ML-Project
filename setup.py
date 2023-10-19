#setup.py will help to set up this project as a local package(means can import anything from any kinds of folder)
# when we install setup.py it will isntall folder as local package
#if not set as local package env get confused whr is this path is located
# so to install all folder as local package using setup.py


import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project"
AUTHOR_USER_NAME = "Bhoomika-gp"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "bhoomikagp7@gmail.com"

#setup.py by default code
#find out every folder n install it as local package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)