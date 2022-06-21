from distutils.core import setup
import os

setup(
    name         = 'scanify',
    version      = '0.0.1',
    author       = 'Daniel D. Zhang',
    author_email = 'dzhang.idf@gmail.com',
    license      = 'BSD-3',
    description  = 'A command line for applying image scanning effect',
    url          = 'https://github.com/idf/scanify',
    packages     = [
        'core',
    ],
    scripts          = ['scanify'],
    install_requires = [
        'cycler==0.10.0',
        'decorator==4.0.11',
        'docopt==0.6.2',
        'matplotlib==2.0.0',
        'networkx==1.11',
        'numpy==1.22.0',
        'olefile==0.44',
        'Pillow==4.1.0',
        'pyparsing==2.2.0',
        'python-dateutil==2.6.0',
        'pytz==2017.2',
        'PyWavelets==0.5.2',
        'scikit-image==0.13.0',
        'scipy==0.19.0',
        'six==1.10.0',
    ]
)