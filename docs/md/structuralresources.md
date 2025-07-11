[HOME](../../README.md)

# Structural resources

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
