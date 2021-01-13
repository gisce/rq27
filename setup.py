"""
rq is a simple, lightweight, library for creating background jobs, and
processing them.
"""
import os
from setuptools import setup, find_packages


def get_version():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'rq/version.py')) as f:
            locals = {}
            exec(f.read(), locals)
            return locals['VERSION']
    except IOError:
        raise RuntimeError('No version info found.')


def get_requirements():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'requirements.txt')) as f:
            return f.readlines()
    except IOError:
        raise RuntimeError('No requirements info found.')


setup(
    name='rq27',
    version=get_version(),
    url='https://github.com/openoriented/rq27',
    license='BSD',
    author='Vincent Driessen',
    author_email='vincent@3rdcloud.com',
    description='RQ is a simple, lightweight, library for creating background '
                'jobs, and processing them.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=get_requirements(),
    #python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'rq = rq.cli:main',

            # NOTE: rqworker/rqinfo are kept for backward-compatibility,
            # remove eventually (TODO)
            'rqinfo = rq.cli:info',
            'rqworker = rq.cli:worker',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring',

    ]
)
