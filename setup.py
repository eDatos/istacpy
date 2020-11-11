from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='istacpy',
    version='0.4.2',
    packages=find_packages(exclude=('tests',)),
    url='https://www.gobiernodecanarias.org/istac/api/',
    license='gpl-3.0',
    author='Instituto Canario de Estadistica (ISTAC)',
    author_email='consultas.istac@gobiernodecanarias.org',
    description=(
        'Python package for obtaining open data '
        'from Instituto Canario de Estadística (ISTAC)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['istacpy', 'ISTAC', 'Instituto Canario de Estadistica', 'API', 'JSON'],
    install_requires=['requests'],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
