from setuptools import setup, find_packages

setup(
    name="voodoo-gui",
    version="0.1.1",
    description="A Python library to create UIs like Streamlit but with simple syntax",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="yusuf karatoprak",
    author_email="yusuf.karatoprak@gmail.com",
    url = "https://github.com/yusufkaratoprak/voodoopy",
    packages=find_packages(),  # Automatically find packages in the directory
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Flask",
        "requests",
        "flask_cors"
    ],
    )
