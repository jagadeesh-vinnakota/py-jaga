import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-vinnakota",
    version="0.0.2",
    author="Jagadeesh Vinnakota",
    author_email="jagadeesh.vinnakota93@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jagadeesh-vinnakota/py-jaga",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
