from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="istacpy",
    version="0.3",
    packages=["istacpy.indicators", "istacpy.structuralresources", "istacpy.statisticalresources", "istacpy.resources"],
    url="https://www.gobiernodecanarias.org/istac/api/",
    download_url="https://github.com/eDatos/istacpy/raw/master/dist/istacpy-0.3.tar.gz",
    license="gpl-3.0",
    author="Instituto Canario de Estadistica (ISTAC)",
    author_email="consultas.istac@gobiernodecanarias.org",
    description="Python package for obtaining open data from Instituto Canario de Estadistica (ISTAC)",
    long_description=long_description,
    keywords=["istacpy", "ISTAC", "Instituto Canario de Estadistica", "API", "JSON"],
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
