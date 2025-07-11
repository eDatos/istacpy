[HOME](../../README.md)

# Error handling

## Custom exceptions

There are a bunch of custom exceptions defined in the package.

> **On the shoulder of gigants**
>
> Special mention to API requests handling. Behind the scenes, this package uses well-known [`requests`](https://requests.readthedocs.io/en/master) package to retrieve data from API. [Different errors](https://requests.readthedocs.io/en/master/_modules/requests/exceptions/) can happen and they are raised to be captured for the user.

It's important to say that these exceptions will include a custom field called `requested_url` that let's the user to handle the API url.

## Debug mode

Debug mode can be enabled using the proper function:

```python
    from istacpy import services
    services.set_debug()
```

Amongh other side effects, when debug mode is enabled, API urls are displayed when a query is performed:

```pycon
    >>> indicators.get_subjects()
    https://datos.canarias.es/api/estadisticas/indicators/v1.0/subjects
    (('011', 'Territorio y usos del suelo'),
     ('012', 'Medio ambiente'),
     ('021', 'Población'),
     ('022', 'Movimiento natural'),
     ('023', 'Movimientos migratorios'),
     ('031', 'Calidad de vida'),
     ('033', 'Educación'),
     ('036', 'Justicia y seguridad'),
     ('041', 'Cuentas económicas'),
     ('042', 'Precios, consumo e inversión'),
     ('043', 'Empresas y centros de trabajo'),
     ('051', 'Empleo'),
     ('061', 'Agricultura, ganadería, pesca y caza'),
     ('071', 'Industria, energía y agua'),
     ('072', 'Construcción y vivienda'),
     ('080', 'SECTOR SERVICIOS'),
     ('081', 'Comercio'),
     ('082', 'Hostelería y turismo'),
     ('083', 'Transporte y comunicaciones'),
     ('084', 'Servicios financieros, monetarios y seguros'),
     ('091', 'Administración pública'))  
```

Debug can be disabled as well. For that end, you can use the function `services.set_nodebug()`.
