import os

from setuptools import setup, find_packages


CURRNET_DIR = os.path.dirname(os.path.realpath(__file__))


with open(os.path.join(CURRNET_DIR, 'README.rst')) as readme:
    long_description = readme.read()


setup(
    name="Flask-BearyChat",
    version="0.1.0",
    url="https://github.com/shonenada/flask-bearychat",
    author="Yaoda Liu",
    author_email="shonenada@gmail.com",
    description="A Flask extension to help interact with BearyChat",
    long_description=long_description,
    zip_safe=False,
    packages=find_packages(exclude=["docs"]),
    license="MIT",
    platform="any",
    include_package_data=True,
    install_requires=[
        "Flask",
        "six"
    ],
    tests_requires=[
        "pytest",
        "pytest-pep8",
        "pytest-cov",
    ],
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
