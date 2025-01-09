from setuptools import setup, find_packages

setup(
    name='google-generativeai',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'google-auth-httplib2',
        'google-auth-oauthlib'
    ]
)