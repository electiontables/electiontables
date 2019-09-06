from distutils.core import setup

setup(
    name='electiontables',
    version='0.1.0',
    author='Vadim Kantorov, Alexander Shpilkin',
    author_email='vadimkantorov@gmail.com',
    packages=['electiontables'],
    url='https://github.com/electiontables/electiontables',
    description='Election tables utils',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy",
    ],
)
