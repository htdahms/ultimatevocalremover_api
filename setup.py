import os
from distutils.core import setup
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

install_requires = [
    req for req in required if not req.startswith('git+')
]

# Fixed pyrubberband
dependency_links = [
    'https://github.com/jhj0517/pyrubberband.git#egg=pyrubberband'
]

setup(
   name='uvr',
   version='0.1',
   description='Universal Voice Remover API',
   authors='Mohannad Barakat',
   author_email="Mohannad.Barakat@fau.de",
   license='MIT',
   package_dir={'uvr':'src'},
   long_description=open('README.md', encoding='utf-8').read(),
   install_requires=install_requires,
   dependency_links=dependency_links,
   url="https://github.com/NextAudioGen/ultimatevocalremover_api.git",
   package_data={
       'uvr': ['**/*.txt', '**/*.t7', '**/*.pth', '**/*.json', '**/*.yaml', '**/*.yml']
   }
)