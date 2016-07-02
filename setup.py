"""
Flask-Redislite
---------------

Using Flask with Redislite
"""
import io
from setuptools import setup

with io.open('README.rst', encoding='utf-8') as f:
    description = f.read()
with io.open('HISTORY.rst', encoding='utf-8') as f:
    description += "\n\n%s" % f.read()

setup(
    name='Flask-Redislite',
    version='0.0.2',
    url='https://github.com/scattm/FlaskRedislite',
    download_url='https://github.com/scattm/FlaskRedislite',
    license='MIT',
    author='Trong-Nghia Nguyen',
    author_email='ntngh2712@gmail.com',
    maintainer='Trong-Nghia Nguyen',
    maintainer_email='ntngh2712@gmail.com',
    description='Using Flask with Redislite',
    long_description=__doc__,
    py_modules=['flask_redislite'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'redislite'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)