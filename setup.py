import os, sys

from setuptools import setup, find_packages
from setuptools.command.install import install

script_path = os.path.join(sys.prefix, "bin")

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    def run(self):
        os.system("chmod +x " + os.path.join(script_path, "CytoSig_run.py"))
        install.run(self)


setup(
    name="CytoSig",
    version="0.1.0dev",
    author="Peng Jiang",
    author_email="peng.jiang@nih.gov",
    description="Prediction model for cytokine signaling activity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/data2intelligence/CytoSig",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # TODO this doesn't match `LICENSE`
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pandas",
        # Fix for https://github.com/data2intelligence/ridge_significance/pull/1
        "ridge_significance @ git+https://github.com/grst/ridge_significance.git@main",
    ],
    extras_require={
        "test": ["pytest"],
        "scanpy": ["anndata"]
    },
    data_files=[
        (
            "bin",
            [
                os.path.join("CytoSig", "CytoSig_run.py"),
                os.path.join("CytoSig", "signature.centroid"),
                os.path.join("CytoSig", "signature.centroid.expand"),
            ],
        ),
    ],
    cmdclass={
        "install": PostInstallCommand,
    },
)
