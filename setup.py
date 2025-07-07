from setuptools import setup, find_packages

setup(
    name="bodhi_sdk",
    version="0.1.0-alpha",
    author="Project Bodhi Tree Team",
    description="A simulation of the GCLM v3.0, a new AI architecture for creative synthesis.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bodhi-tree-ai/project-bodhi-tree", # Simulated URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy",
    ],
)
