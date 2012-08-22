from setuptools import setup, find_packages

import cms


setup(
    author="noxan",
    author_email="noxan@redmoonstudios.de",
    name="django-mini-cms",
    version=cms.__version__,
    description="Minimalistic django cms",
    url="https://github.com/noxan/django-mini-cms",
    license='BSD License',
    platforms=['OS Independent'],
    install_requires=[
        'Django>=1.4',
    ],
    packages=find_packages(),
)
