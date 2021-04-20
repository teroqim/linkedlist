from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='linkedlist',
     version='2.0.0',
     description='General purpose linked list',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/teroqim/linkedlist',
     author='Peter Andersson',
     author_email='teroqim@gmail.com',
     packages=['linkedlist'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     zip_safe=False
)
