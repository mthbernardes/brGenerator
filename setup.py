# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='brGenerator',
    version='1.2',
    url='https://github.com/mthbernardes/brGenerator',
    license='MIT License',
    author='Matheus Bernardes',
    author_email='mthbernardes@gmail.com',
    keywords='gerador pessoas',
    description=u'Modulo para gerar informações de pessoas, util para automação de cadastros/',
    packages=['brGenerator'],
    install_requires=['requests','lxml'],
)
