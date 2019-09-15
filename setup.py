from setuptools import setup

setup(
    name='coosa-control',
    version='0.1.0',
    description='Control script for coosa smart plugs',
    url='https://github.com/matthewscholefield/coosa-control',
    author='Matthew D. Scholefield',
    author_email='matthew331199@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='coosa control',
    py_modules=['coosa_control'],
    install_requires=[
        'appdirs'
    ],
    entry_points={
        'console_scripts': [
            'coosa-control=coosa_control:main'
        ],
    }
)
