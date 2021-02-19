from setuptools import setup

setup(
    name="bscscan-python",
    version="0.0.1",
    description="A python API for bscscan.com.",
    url="https://github.com/pcko1/bscscan-python",
    author="Panagiotis-Christos Kotsias",
    author_email="kotsias.pan@gmail.com",
    license="MIT",
    packages=[
        "bscscan",
        "bscscan.configs",
        "bscscan.enums",
        "bscscan.modules",
        "bscscan.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
