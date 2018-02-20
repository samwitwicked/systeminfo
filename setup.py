'''
Created on 20-Feb-2018

@author: sam
'''
from setuptools import setup

setup(name="systeminfo", 
      version="0.1", 
      description="Basic System information for COMP30670",
      url="",
      author= "Abishek Sambandh", 
      author_email="abishek.kumar@ucdconnect.ie",
      license="GPL3",
      packages=["systeminfo"],
      entry_points={'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
                    }
      )
