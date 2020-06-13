from distutils.core import setup
with open("README.md",'r') as fh:
    long_description = fh.read()

setup(
    name='Panku-Skynse',
    scripts=['Panku/panku'],
    version='0.1',
    packages=['Panku'],
    license='MIT',
    author='Skynse',
    long_description=long_description,
    package_data={'': ['./requirements.txt']},
    include_package_data=True,
    author_email='',
    description='Easy API-less reddit scraper',
    python_requires='>=3.6',
)
