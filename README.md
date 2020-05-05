<span>
  <p><a href="https://pypi.org/project/istacpy/">istacpy</a> is a Python package for obtaining open data from Instituto Canario de Estadistica (ISTAC)</p>
</span>


<span>

<h3>How to install</h3>
<div>
  <code>
    pip install istacpy
  </code>
</div>

<h3>Access to indicators</h3>
<p> API URL: <a href="https://www3.gobiernodecanarias.org/istac/api/indicators/v1.0/">https://www3.gobiernodecanarias.org/istac/api/indicators/v1.0/</a></p>
<div>
  <p><strong>Example 1</strong>: Get a list of indicators published in the ISTAC-indicators database</p>
  <code>
    from istacpy.indicators import geographic
  </code>
  <br>
  <code>
    geographic.get_indicators_geographic_granularities()
  </code>
  <br><br>
  <p><strong>Example 2</strong>: Get a list of geographic granularities treated in the ISTAC-indicators database. For example provincial, insular or municipal granularity</p>
  <code>
    from istacpy.indicators import indicators
  </code>
  <br>
  <code>
    indicators.get_indicators()
  </code>
</div>

<h3>Access to statistical resources</h3>
<p> API URL: <a href="https://www3.gobiernodecanarias.org/istac/api/statistical-resources/v1.0/">https://www3.gobiernodecanarias.org/istac/api/statistical-resources/v1.0/</a></p>
<div>
  <p><strong>Example 1</strong>: Get all existing statistical data cubes</p>
  <code>
    from istacpy.statisticalresources import cubes
  </code>
  <br>
  <code>
    cubes.get_statisticalresources_datasets()
  </code>
  <br><br>
  <p><strong>Example 2</strong>: Get all the data sets maintained by a certain organization</p>
  <code>
    from istacpy.statisticalresources import cubes
  </code>
  <br>
  <code>
    cubes.get_statisticalresources_datasets_agency(agencyid = "ISTAC")
  </code>
</div>

<h3>Access to structural resources</h3>
<p> API URL: <a href="https://www3.gobiernodecanarias.org/istac/api/structural-resources/v1.0/">https://www3.gobiernodecanarias.org/istac/api/structural-resources/v1.0/</a></p>
<div>
  <p><strong>Example 1</strong>: Get a list of classifications</p>
  <code>
    from istacpy.structuralresources import classifications
  </code>
  <br>
  <code>
    classifications.get_structuralresources_codelists()
  </code>
  <br><br>
  <p><strong>Example 2</strong>: Get a list of geographic coordinate from Icod de los Vinos (Municipality)</p>
  <code>
    from istacpy.structuralresources import variables
  </code>
  <br>
  <code>
    variables.get_structuralresources_geoinfo("VR_TERRITORIO", "MUN_ICOD_VINOS")
  </code>
</div>

</span>
<br>


<span>
  <p>Latest <strong>version</strong> is istacpy-<strong>0.3</strong></p>
  <p>Contact us at <a href="mailto:edatos.istac@gobiernodecanarias.org">Instituto Canario de Estadística (ISTAC)</a>
</span>
