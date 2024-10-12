
from setuptools import setup, find_packages

setup(
    name="voodoo-gui",
    version="0.1",
    description="A Python library to create UIs like Streamlit but with simple syntax",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask", # Flask framework for serving web pages
        "requests",
        "flask_cors"
    ],
    entry_points={
        "console_scripts": [
            "voodoo-gui = voodoo.gui:main",
        ]
    },
    python_requires=">=3.6",
)
    