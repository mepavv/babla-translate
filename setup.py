from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="babla_translate",
    version=1.0,
    license="MIT",
    author="Michał Pawłowski",
    author_email="<michal.paw000@gmail.com>",
    url='https://github.com/mepavv/babla_translate',
    description='A module for translating words and generating examples using Bab.la dictionary.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    keywords=['translation','scraper', 'api'],
    classifiers=["License :: OSI Approved :: MIT License"],
)