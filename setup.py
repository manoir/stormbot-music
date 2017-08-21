#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot-music',
      version='1.2',
      description='music plugin for stormbot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot/stormbot-music',
      packages=find_packages(),
      install_requires=['stormbot'],
      entry_points={'stormbot.plugins': ['music = stormbot_music:Music']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
