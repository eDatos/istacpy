from setuptools import setup

setup(
    name="istacpy",
    version="0.1",
    packages=["istacpy.indicators", "istacpy.structuralresources", "istacpy.statisticalresources"],
    url="https://www.gobiernodecanarias.org/istac/api/",
    license="GPLv3",
    author="Instituto Canario de Estadistica (ISTAC)",
    author_email="consultas.istac@gobiernodecanarias.org",
    description="Python package for obtaining open data from Instituto Canario de Estadistica (ISTAC)"
)
