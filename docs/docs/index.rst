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

* :ref:`istacpy.indicators`: Systems, instances, granularities and subjects of indicators.
* :ref:`istacpy.statisticalresources`: Datasets and queries of cubes.
* :ref:`istacpy.structuralresources`: Categories, schemes, classifications, families and concepts for normalize statistical resources.
* :ref:`Error handling`
   
.. toctree::
   :hidden:
   :maxdepth: 2
   
   istacpy.indicators
   istacpy.statisticalresources
   istacpy.structuralresources
   error_handling 
