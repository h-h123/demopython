from setuptools import setup, find_packages

setup(
    name="tkinter_sqlite_app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "tkinter",
        "sqlite3"
    ]
)
