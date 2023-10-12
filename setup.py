from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name='fourdle',
    version='0.1.2',
    description='A package for fourdle game logic',
    author='Filip Cederquist',
    author_email='cederquist94@hotmail.com',
    license="MIT",
    url='https://github.com/cerre/fourdlegame',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10'
    ],
)
