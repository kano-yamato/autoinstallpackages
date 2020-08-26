#!/usr/bin/env python3
from setuptools import setup

setup(
    name="package-auto-install",
    version="1.0.0",
    entry_points={
        "console_scripts" : [
            "packins = autoinstall:main"
        ]
    }
)
