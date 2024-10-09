from setuptools import setup, find_packages

setup(
    name='transfile-cli',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'transfile = transfile.translate:main'  # Adjusting to point to the main function in the translate module
        ],
    },
)
