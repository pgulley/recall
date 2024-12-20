from setuptools import setup, find_packages

setup(
    name="recall",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "invoke",  # Add any other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "recall=recall.tasks:main",  # Entry point for the CLI
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)