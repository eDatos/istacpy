.. _istacpy.structuralresources:

####################
Structural resources
####################

Structural resources serve as support to normalize statistical resources produces by the organization. The main existing structural resources are organization schemes, topic schemes, concept schemes, classifications and definitions of data structures.

**Example 1**: Get a list of classifications::

    from istacpy.structuralresources import classifications
    classifications.get_structuralresources_codelists()

**Example 2**: Get a list of geographic coordinate from `Icod de los Vinos <https://www.icoddelosvinos.es/>`_::

    from istacpy.structuralresources import variables
    variables.get_structuralresources_geoinfo('VR_TERRITORIO', 'MUN_ICOD_VINOS')

************************************
istacpy.structuralresources.category
************************************

.. automodule:: istacpy.structuralresources.category
    :members:
    :undoc-members:

*******************************************
istacpy.structuralresources.classifications
*******************************************

.. automodule:: istacpy.structuralresources.classifications
    :members:
    :undoc-members:

************************************
istacpy.structuralresources.concepts
************************************

.. automodule:: istacpy.structuralresources.concepts
    :members:
    :undoc-members:

******************************************
istacpy.structuralresources.datastructures
******************************************

.. automodule:: istacpy.structuralresources.datastructures
    :members:
    :undoc-members:

*************************************
istacpy.structuralresources.variables
*************************************

.. automodule:: istacpy.structuralresources.variables
    :members:
    :undoc-members:
