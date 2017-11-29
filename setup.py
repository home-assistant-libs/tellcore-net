from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

VERSION = "0.2"

setup(
    name='tellcore-net',
    version=VERSION,
    license='BSD License',
    author='Pascal Vizeli',
    author_email='pvizeli@syshack.ch',
    url='https://github.com/pvizeli/tellcore-net',
    download_url='https://github.com/pvizeli/tellcore-net/tarball/'+VERSION,
    description=('a Python module that allow to run tellcore over TCP/IP'),
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    keywords=['telldus', 'tellcore', 'interface', 'wrapper', 'socat'],
    zip_safe=False,
    platforms='any',
    py_modules=['tellcorenet'],
)
