##########
pprint-36
##########

.. start short_desc

**Backport of pprint from Python 3.9 to Python 3.6-3.8**

.. end short_desc

See the `Python documentation <https://docs.python.org/3/library/pprint.html>`_ for examples and usage information.


The pertinent changes from Python 3.6 to Python 3.9 are:

* ``pprint`` can now pretty-print ``types.SimpleNamespace``.
  Contributed by Carl Bordum Hansenin Python 3.9.

* ``pprint.pp`` has been added to pretty-print objects with dictionary
  keys being sorted with their insertion order by default. Parameter
  *sort_dicts* has been added to ``pprint.pprint``, ``pprint.pformat`` and
  ``pprint.PrettyPrinter``. Contributed by Rémi Lapeyre in Python 3.8.


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/pprint36/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/pprint36/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/pprint36/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/pprint36/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/pprint36/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/pprint36/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/pprint36/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/pprint36/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/pprint36/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/pprint36/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/domdfcoding/pprint36/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/pprint36/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/pprint36/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/pprint36?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/pprint36?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/pprint36
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/pprint36
	:target: https://pypi.org/project/pprint36/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pprint36?logo=python&logoColor=white
	:target: https://pypi.org/project/pprint36/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pprint36
	:target: https://pypi.org/project/pprint36/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/pprint36
	:target: https://pypi.org/project/pprint36/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/pprint36
	:target: https://github.com/domdfcoding/pprint36/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/pprint36
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/pprint36/v3.9.0.2
	:target: https://github.com/domdfcoding/pprint36/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/pprint36
	:target: https://github.com/domdfcoding/pprint36/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/pprint36
	:target: https://pypi.org/project/pprint36/
	:alt: PyPI - Downloads

.. end shields

|

Installation
--------------

.. start installation

``pprint36`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install pprint36

.. end installation
