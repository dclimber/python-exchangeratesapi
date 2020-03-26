import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-exchangeratesapi",
    version="0.0.2",
    author="Dastan Abdrakhmanov",
    author_email="dastand.climber@gmail.com",
    description="Simple python api wrapper for exchangeratesapi.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dclimber/python-exchangeratesapi",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
