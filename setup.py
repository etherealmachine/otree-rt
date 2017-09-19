import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='otree-redwood',
    version='0.4.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='oTree extension for inter-page communication.',
    long_description=README,
    url='https://github.com/Leeps-Lab/otree-redwood',
    author='James Pettit',
    author_email='james.l.pettit@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Sphinx',
        'sphinx-autobuild',
        'sphinx-rtd-theme',
        'asgi_redis>=1.2.0,<2',
        'chan>=0.3.1,<1',
        'channels>=1.1.3,<2',
        'daphne>=1.0.0,<2',
        'Django=1.8.8',
        'jsonfield>=2,<3',
        'mockredispy>=2.9.0,<3',
				'otree-core==1.4.0b6',
    ]
)
