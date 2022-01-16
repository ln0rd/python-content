### Study Projects with Python 🐍

This repository is a compiled content about Python.

Projetcs:

- Flask api
  - Basic content
  - Token jwt
  - Rest api
- Django Project
- Django Simple Mock

#### Dependencies

I'm using pipenv to manager the Dependencies and python version, so check that [`pipenv`](https://pipenv.pypa.io/en/latest/) it was installed.
To run use:

```
pipenv run python your_file
```

#### Some commands

to see from pip all dependencies installed in that version of pip run:

```
pip3.5 freeze | pip freeze
```

#### Installing and using virtualenv

to install use the pip most updated and them:

```
pip3.5 install virtualenv
```

and to use and version of python using a virtual env run:

```
virtualenv venv --python=python3.9
```

after this It will create in your folder that you executed the virtualenv a folder called venv
it contains the python version that you installed, so to use it just run:

```
source venv/bin/activate
```

to exit from virtual env run:

```
deactivate
```
