Getting Started
===============

Install prerequisites::

  pip install numpy scipy matplotlib pillow
  pip install setuptools Sphinx numpydoc

Install this package in development mode::

  python setup.py develop

Run unit tests::

  cd xy_python_utils
  python -m unittest discover -p "*_test.py"
  cd ..

Generate documentation::

  cd docs
  make html
  cd ..
