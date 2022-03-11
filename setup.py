from setuptools import setup

setup(
    name='gtranslate-cli',
    version='0.1.0',
    packages=['gtranslate'],
    entry_points={
        'console_scripts': [
            'gtranslate = gtranslate.__main__:main',
            'gtd = gtd.__main__:main'
        ]
    })
