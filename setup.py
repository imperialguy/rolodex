from setuptools import setup, find_packages

requires = [
    'coverage==4.0',
    'PyYAML==3.11',
    'unittest2==1.1.0',
    'six==1.10.0',
    'traceback2==1.4.0',
    'linecache2==1.0.0',
    'nose==1.3.7'
]

tests_require = requires

setup(name='rolodex',
      version='0.1',
      description='rolodex app for percolate',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Ven Karri',
      author_email='vpkcareer2011@gmail.com',
      url='',
      keywords='rolodex percolate programming challenge',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      install_requires=requires,
      tests_require=tests_require,
      )
