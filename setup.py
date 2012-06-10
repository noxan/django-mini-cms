from setuptools import setup, find_packages


setup(
    author="noxan",
    author_email="noxan@redmoonstudios.de",
    name="django-mini-cms",
    version="0.0.1",
    description="Minimalistic django cms",
    url="https://github.com/noxan/django-mini-cms",
    install_requires=[
        'Django>=1.4',
    ],
    packages=find_packages(),
)