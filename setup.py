# -*- coding: utf-8 -*-
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

__author__ = "Sergi Blanch-Torne"
__email__ = "srgblnchtrn@protonmail.ch"
__copyright__ = "Copyright 2016, Sergi Blanch-Torne"
__license__ = "GPLv3+"


from setuptools import setup, find_packages
from nebel import version


setup(name = 'nebel',
      license = "GPLv3+",
      description = "middleware for IIoT",
      version = version.version(),
      author = "Sergi Blanch-Torn\'e",
      author_email = "srgblnchtrn@protonmail.ch",
      classifiers = ['Development Status :: 1 - Planning',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Science/Research',
                     'Intended Audience :: Information Technology',
                     'License :: OSI Approved :: '\
                        'GNU General Public License v3 or later (GPLv3+)',
                     'Operating System :: POSIX',
                     #'Programming Language :: Cython',
                     'Programming Language :: Python',
                     'Topic :: Scientific/Engineering :: '\
                        'Interface Engine/Protocol Translator',
                     'Topic :: Software Development :: Embedded Systems',
                     'Topic :: Software Development :: Libraries :: '\
                        'Python Modules',
                     ''],
      packages=find_packages(),
      url="https://github.com/srgblnch/scpi",
)

#for the classifiers review see:
#https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
#Development Status :: 1 - Planning
#Development Status :: 2 - Pre-Alpha
#Development Status :: 3 - Alpha
#Development Status :: 4 - Beta
#Development Status :: 5 - Production/Stable
