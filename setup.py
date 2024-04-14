from setuptools import setup, find_packages
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()
setup(
    name='SongSwitch',
    version='0.1',
    packages=find_packages(),
    description='SongSwitch is a CLI tool to move Music Libraries between different music streaming '
                'services, Currently supporting Spotify To Tidal',
    long_description=open('README.md').read(),
    url='https://github.com/AHES03/SongSwitch',
    author='Hadi El-Seyed',
    install_requires=read_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='sample setuptools development',
    python_requires='>=3.6',
)
