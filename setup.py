from setuptools import setup
with open("README.md","r") as fh:
     longDescript = fh.read()
setup(
     name="BinaryCounters",
     version='0.0.1',
     description="array based binary counters with useful functions attached",
     long_description=longDescript,
     long_description_content_type="text/markdown",
     py_modules=["BinaryCounters"],
     package_dir={'': 'src'},
     url="https://github.com/altruios/BinaryCounters",
     author="paul kosmala",
     author_email="paul.kosmala@gmail.com",
     #install_requires=['numpy',],
     classifiers=[
          'Development Status :: 1 - Planning',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
    ],
)