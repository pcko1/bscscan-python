from setuptools import setup

setup(
    name="bscscanscan-python",
    version="2.0.2",
    description="A python API for bscscan.com.",
    url="https://github.com/pcko1/bscscanscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "bscscanscan",
        "bscscanscan.configs",
        "bscscanscan.enums",
        "bscscanscan.modules",
        "bscscanscan.utils",
    ],
    install_requires=["requests", "coverage"],
    include_package_data=True,
    zip_safe=False,
)
