from setuptools import setup, find_packages

setup(
    name="big_o_estimator",
    version="0.1.0",
    description="A simple package to estimate the Big-O complexity of Python functions.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/big_o_estimator",  # Replace with your GitHub repository
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
