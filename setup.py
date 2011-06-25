from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='silva.app.photogallery',
      version=version,
      description="Render photo galleries in Silva",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='silva photo gallery',
      author='Sylvain Viollon',
      author_email='info@infrae.com',
      url='',
      license='BSD',
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['silva', 'silva.app'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'five.grok',
        'setuptools',
        'silva.core.conf',
        'silva.core.interfaces',
      ],
      )
