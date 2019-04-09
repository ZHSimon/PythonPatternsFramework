import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tgpatternsframework-zacksimon",
    version="0.1.2",
    author="Zack Simon",
    author_email="zack.simon+thraxisgames@gmail.com",
    description="A series of python programming patterns to extend",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)