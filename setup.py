from setuptools import setup
from setuptools import find_packages

setup(
    name='dcard_coworker',
    description='',
    long_description=open('README.rst').read(),
    version='0.0.1',
    author='carlcarl',
    author_email='carlcarlking@gmail.com',
    url='https://github.com/carlcarl/dcard_coworker',
    packages=find_packages(),
    license='MIT',
    package_data={
    },
    entry_points={
    },
    keywords = ['dcard', 'crawler', 'coroutine'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
    ],
)
