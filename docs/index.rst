#######
istacpy
#######

**istacpy** is a Python package for obtaining open data from `Instituto Canario de Estadística (ISTAC) <http://www.gobiernodecanarias.org/istac/>`_. It provides a wrapper to the `open API catalog <https://www3.gobiernodecanarias.org/aplicaciones/appsistac/api>`_.

.. image:: https://raw.githubusercontent.com/eDatos/istacpy/master/istacpy-logo.svg

************
Installation
************

.. code-block:: shell

   pip install istacpy

*****
Usage
*****

The package is divided into several modules depending on the resource you want to retrieve:

.. toctree::
   :maxdepth: 2

   istacpy.indicators
   istacpy.statisticalresources
   istacpy.structuralresources

**************
Error handling
**************

There are a bunch of custom exceptions defined in the package:

.. automodule:: istacpy.exceptions
    :members:
    :undoc-members:

On the shoulder of gigants
==========================

Special mention to API requests handling. Behind the scenes, this package uses well-known `requests <https://requests.readthedocs.io/en/master/>`_ package to retrieve data from API. `Different errors <https://requests.readthedocs.io/en/master/_modules/requests/exceptions/>`_ can happen and they are raised to be captured for the user.

It's important to say that these exceptions will include a custom field called ``requested_url`` that let's the user to handle the API url.
