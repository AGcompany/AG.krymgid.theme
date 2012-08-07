from setuptools import setup, find_packages
import os

version = '1.0.0'

setup(name='AG.krymgid.theme',
      version=version,
      description="AG.krymgid.theme package",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Bogdan Girman',
      author_email='bogdan.girman@gmail.com',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src',exclude=['ez_setup']),
      package_dir = {'': 'src'},
      namespace_packages=['AG', 'AG.krymgid'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
