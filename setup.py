import codecs
from setuptools import setup


def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    'docopt >= 0.6.1, < 0.7',
]


setup(
    name="banking4converter",
    version=find_version("converter", "__init__.py"),
    description="Converter for banking4 formats",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/patrickjahns/banking4converter",
    author="Patrick Jahns",
    author_email="github@patrickjahns.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Environment :: Console',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["banking4converter"],
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    entry_points={"console_scripts": ["banking4converter=converter.cli.main:main"]},
)