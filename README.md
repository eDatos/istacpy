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

```python
from istacpy.indicators import indicators
indicators.get_indicators()
```

**Example 2**: Get a list of geographic granularities treated in the ISTAC-indicators database. For example provincial, insular or municipal granularity:

```python
from istacpy.indicators import geographic
geographic.get_indicators_geographic_granularities()
```

#### `istacpy.indicators.lite`

This is a lite version of the rest of the indicators API. It’s a kind of wrapper to facilitate the access to indicators data. It’s not as powerful as the above functions but it hides a lot of the business logic of the API, so it’s quite suitable to quickly retrieve information.

### Statistical resources

**Example 1**: Get all existing statistical data cubes:

```python
from istacpy.statisticalresources import cubes
cubes.get_statisticalresources_datasets()
```

**Example 2**: Get all the data sets maintained by a certain organization:

```python
from istacpy.statisticalresources import cubes
cubes.get_statisticalresources_datasets_agency(agencyid='ISTAC')
```

### Structural resources

**Example 1**: Get a list of classifications:

```python
from istacpy.structuralresources import classifications
classifications.get_structuralresources_codelists()
```

**Example 2**: Get a list of geographic coordinate from [Icod de los Vinos](https://www.icoddelosvinos.es/):

```python
from istacpy.structuralresources import variables
variables.get_structuralresources_geoinfo('VR_TERRITORIO', 'MUN_ICOD_VINOS')
```

## Documentation

For a full documentation of all available functions within the package, please see http://istacpy.readthedocs.io/

## Bugs/Requests

Please use the [GitHub issue tracker](https://github.com/eDatos/istacpy/issues) to submit bugs or request features.

## Changelog

Consult the [Changelog](CHANGELOG.md) page for fixes and enhancements of each version.

## Contact

You can also contact us via email at [edatos.istac@gobiernodecanarias.org](mailto:edatos.istac@gobiernodecanarias.org).

## License

Copyright Instituto Canario de Estadística (ISTAC), 2018.

Distributed under the terms of the [GPLv3](LICENSE) license, istacpy is free and open source software.
