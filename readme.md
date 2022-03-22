# Veeam Client

Veeam Rest API Client or wrapper to make it easier to interact with the Veeam API.

[The Veeam API documentation](https://helpcenter.veeam.com/backup/rest/overview.html)

## Installation

    pip install veeam

## Usage

    from veeam.client import VeeamClient
    
    client = VeeamClient()
    
### Supply your own session

**Ensure the url ends in `/api`**

    from veeam.client import VeeamClient 
    from requests import Session 

    session = Session()
    session.headers.update({'token': 'ABCDE'}) 

    client = VeeamClient(
        url='https://api.veeam.example/api', 
        veeam_username='admin', 
        veeam_password='pazzw0rd', 
        session=session
    )


## Uploading to Pypi

Make sure to bump the version in `setup.py`

Create the `dist` and `build` folders

    python setup.py sdist bdist_wheel

Upload to test pypi

    twine upload --repository testpypi dist/*

Upload to real pypi

    twine upload --repository pypi dist/*

## Testing the Library

You can use the package from the test pypi with:

    pip install -i https://test.pypi.org/simple/ veeam

## Running Tests

    pytest

## Contributing

Original module written by surfer190 (https://github.com/surfer190/veeam)
Update added and published by steve-daedilus

Unless or until surfer190 is able to progress anything on this module, I'll do my best to tick it over.
...