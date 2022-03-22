import setuptools

with open('readme.md') as f:
    long_description = f.read()

setuptools.setup(
    name='veeam',
    version='0.1.6',
    description='Veeam backup API Client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=['requirements', 'tests', ]),
    author_email='steve@daedilus.org',
    python_requires='>=3.6',
    install_requires=['requests', ],
    author='steve-daedilus',
    url='https://github.com/steve-daedilus/veeam.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent', 
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English'
    ]
)
