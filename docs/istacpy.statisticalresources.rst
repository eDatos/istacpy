#####################
Statistical resources
#####################

******************
Dataframe handling
******************

Apart from all the functions below, there are **two special calls** we can use in order to get a `pandas DataFrame`_  instead of the usual json API response:

- :func:`istacpy.statisticalresources.queries.get_statisticalresources_queries_agency_resource`
- :func:`istacpy.statisticalresources.cubes.get_statisticalresources_datasets_agency_resource_version`

.. important:: ``pip install pandas`` is required for this feature to work.

Guess you are looking for data about population under 18 in Canary Islands regarding its employment status. Once you get the *resource identifier* you could make this query:

.. code-block:: pycon

    >>> from istacpy.statisticalresources import queries

    >>> response = queries.get_statisticalresources_queries_agency_resource(
    ...    agencyid='ISTAC',
    ...    resourceid='C00086B_000006',
    ...    as_dataframe=True
    ... )

    >>> type(response)
    istacpy.services.ResolvedAPIResponse

.. note:: Adding the parameter ``as_dataframe=True`` makes you get a ``ResolvedAPIResponse`` object.

This object provides two attributes: ``dataframe`` and ``codelists``:

.. code-block:: pycon

    >>> response.dataframe
                    MEDIDAS TIME_PERIOD SEXO      SITUACION_ECONOMICA_ICC VALORACION OBSERVACIONES
    0                POBLACION     2018-Q4   _T       ACTUAL_BUSQUEDA_EMPLEO         _T       1791633
    1                POBLACION     2018-Q4   _T       ACTUAL_BUSQUEDA_EMPLEO      IGUAL        782350
    2                POBLACION     2018-Q4   _T       ACTUAL_BUSQUEDA_EMPLEO      MEJOR        272479
    3                POBLACION     2018-Q4   _T       ACTUAL_BUSQUEDA_EMPLEO       PEOR        736804
    4                POBLACION     2018-Q4   _T  EXPECTATIVA_BUSQUEDA_EMPLEO         _T       1791633
    ..                     ...         ...  ...                          ...        ...           ...
    283  POBLACION__PORCENTAJE     2020-Q4    M       ACTUAL_BUSQUEDA_EMPLEO       PEOR         87.10
    284  POBLACION__PORCENTAJE     2020-Q4    M  EXPECTATIVA_BUSQUEDA_EMPLEO         _T        100.00
    285  POBLACION__PORCENTAJE     2020-Q4    M  EXPECTATIVA_BUSQUEDA_EMPLEO      IGUAL         19.25
    286  POBLACION__PORCENTAJE     2020-Q4    M  EXPECTATIVA_BUSQUEDA_EMPLEO      MEJOR         19.35
    287  POBLACION__PORCENTAJE     2020-Q4    M  EXPECTATIVA_BUSQUEDA_EMPLEO       PEOR         61.40

    [288 rows x 6 columns]

    >>> response.codelists
    {'MEDIDAS': {'POBLACION': 'Población',
    'POBLACION__PORCENTAJE': 'Población. Porcentaje'},
    'TIME_PERIOD': {'2020-Q4': '2020 Cuarto trimestre',
    '2020-Q2': '2020 Segundo trimestre',
    '2019-Q4': '2019 Cuarto trimestre',
    '2019-Q2': '2019 Segundo trimestre',
    '2019-Q1': '2019 Primer trimestre',
    '2018-Q4': '2018 Cuarto trimestre'},
    'SEXO': {'_T': 'Ambos sexos', 'M': 'Hombres', 'F': 'Mujeres'},
    'SITUACION_ECONOMICA_ICC': {'ACTUAL_BUSQUEDA_EMPLEO': 'Situación actual para encontrar o mejorar un puesto de trabajo',
    'EXPECTATIVA_BUSQUEDA_EMPLEO': 'Expectativa futura para encontrar o mejorar un puesto de trabajo'},
    'VALORACION': {'_T': 'Total',
    'MEJOR': 'Mejor',
    'IGUAL': 'Igual',
    'PEOR': 'Peor'}}

.. important:: Codelists are mappings between codes and text descriptions. The returned ``response.codelists`` always contains **spanish texts** because they are most cases.


Recoding of downloaded dataset is as easy as:

.. code-block::

    >>> response.dataframe.replace(response.codelists)
                    MEDIDAS            TIME_PERIOD         SEXO                            SITUACION_ECONOMICA_ICC VALORACION OBSERVACIONES
    0                Población  2018 Cuarto trimestre  Ambos sexos  Situación actual para encontrar o mejorar un p...      Total       1791633
    1                Población  2018 Cuarto trimestre  Ambos sexos  Situación actual para encontrar o mejorar un p...      Igual        782350
    2                Población  2018 Cuarto trimestre  Ambos sexos  Situación actual para encontrar o mejorar un p...      Mejor        272479
    3                Población  2018 Cuarto trimestre  Ambos sexos  Situación actual para encontrar o mejorar un p...       Peor        736804
    4                Población  2018 Cuarto trimestre  Ambos sexos  Expectativa futura para encontrar o mejorar un...      Total       1791633
    ..                     ...                    ...          ...                                                ...        ...           ...
    283  Población. Porcentaje  2020 Cuarto trimestre      Hombres  Situación actual para encontrar o mejorar un p...       Peor         87.10
    284  Población. Porcentaje  2020 Cuarto trimestre      Hombres  Expectativa futura para encontrar o mejorar un...      Total        100.00
    285  Población. Porcentaje  2020 Cuarto trimestre      Hombres  Expectativa futura para encontrar o mejorar un...      Igual         19.25
    286  Población. Porcentaje  2020 Cuarto trimestre      Hombres  Expectativa futura para encontrar o mejorar un...      Mejor         19.35
    287  Población. Porcentaje  2020 Cuarto trimestre      Hombres  Expectativa futura para encontrar o mejorar un...       Peor         61.40

    [288 rows x 6 columns]    

.. tip:: This process can also be made for statistical datasets.


************************************
istacpy.statisticalresources.queries
************************************

.. automodule:: istacpy.statisticalresources.queries
    :members:
    :undoc-members:

**********************************
istacpy.statisticalresources.cubes
**********************************

.. automodule:: istacpy.statisticalresources.cubes
    :members:
    :undoc-members:



.. _pandas Dataframe: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
