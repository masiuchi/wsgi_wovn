import os
from distutils.core import setup
from setuptools import setup, find_packages

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(BASE_PATH, 'README.md')).read()

setup(
        name='wsgi_wovn',
        packages=find_packages(),
        version='0.0.1',
        description='WSGI middleware for translating application by WOVN.io.',
        long_description=README,
        author='Masahiro Iuchi',
        author_email='masahiro.iuchi@gmail.com',
        url='https://github.com/masiuchi/wsgi-wovn',
        license='MIT License',
        keywords='wsgi middleware wovn',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Internet :: WWW/HTTP :: WSGI',
            'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Localization',
            ],
        test_suite='tests',
        )
