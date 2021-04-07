![Logo istacpy](https://raw.githubusercontent.com/eDatos/istacpy/master/istacpy-logo.svg)

`istacpy` is a Python package for obtaining open data from [Instituto Canario de Estadística (ISTAC)](http://www.gobiernodecanarias.org/istac/). It provides a wrapper to the [open API catalog](https://www3.gobiernodecanarias.org/aplicaciones/appsistac/api).

## Installation

```console
pip install istacpy
```

## Usage

The package is divided into several modules depending on the resource you want to retrieve.

### Indicators

**Example 1**: Get a list of all available indicators:

```pycon
>>> from istacpy.indicators import indicators
>>> indicators.get_indicators()
```

**Example 2**: Get a list of geographic granularities treated in the ISTAC-indicators database. For example provincial, insular or municipal granularity:

```pycon
>>> from istacpy.indicators import geographic
>>> geographic.get_indicators_geographic_granularities()
```

#### `istacpy.indicators.lite`

This is a lite version of the rest of the indicators API. It’s a kind of wrapper to facilitate the access to indicators data. It’s not as powerful as the above functions but it hides a lot of the business logic of the API, so it’s quite suitable to quickly retrieve information.

**Example**: Get (absolute yearly) population of Lanzarote municipalities between 2010 and 2020:

```pycon
>>> from istacpy.indicators.lite import indicators

>>> indicator = indicators.get_indicator('POBLACION')
>>> data = indicator.get_data(geo='M|Lanzarote', time='Y|2010:2020')

>>> data.as_dataframe()
      Arrecife  Haría  San Bartolomé  Teguise   Tías  Tinajo  Yaiza
2010     58156   5249          18161    20105  19869    5655  14242
2011     57357   5203          18468    20788  20102    5728  14871
2012     56284   5190          18487    21096  20228    5716  15131
2013     55673   4782          18541    21152  20451    5783  15571
2014     56880   4736          18689    21101  19658    5808  15068
2015     56940   4755          18402    21454  20019    5824  15815
2016     58537   4767          18151    21724  20037    5924  15944
2017     59771   4858          18249    21896  19964    6028  16257
2018     61351   4969          18327    22122  20006    6119  16289
2019     62988   5123          18816    22342  20170    6279  16571
2020     64645   5263          19099    22703  20628    6434  17040
```

### Statistical resources

**Example 1**: Get all existing statistical data cubes:

```pycon
>>> from istacpy.statisticalresources import cubes
>>> cubes.get_statisticalresources_datasets()
```

**Example 2**: Get all the data sets maintained by a certain organization:

```pycon
>>> from istacpy.statisticalresources import cubes
>>> cubes.get_statisticalresources_datasets_agency(agencyid='ISTAC')
```

### Structural resources

**Example 1**: Get a list of classifications:

```pycon
>>> from istacpy.structuralresources import classifications
>>> classifications.get_structuralresources_codelists()
```

**Example 2**: Get a list of geographic coordinate from [Icod de los Vinos](https://www.icoddelosvinos.es/):

```pycon
>>> from istacpy.structuralresources import variables
>>> variables.get_structuralresources_geoinfo('VR_TERRITORIO', 'MUN_ICOD_VINOS')
```

## Documentation

For a full documentation of all available functions within the package, please see http://istacpy.readthedocs.io/

## Bugs/Requests

Please use the [GitHub issue tracker](https://github.com/eDatos/istacpy/issues) to submit bugs or request features.

## Changelog

Consult the [Changelog](CHANGELOG.md) page for bugfixes and feature in each version.

## Contact

You can also contact us via email at [edatos.istac@gobiernodecanarias.org](mailto:edatos.istac@gobiernodecanarias.org).

## License

Copyright Instituto Canario de Estadística (ISTAC), 2018.

Distributed under the terms of the [AGPLv3](LICENSE) license, istacpy is free and open source software.
