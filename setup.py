import setuptools
with open("README.md",'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='panku',
    scripts=['bin/panku'],
    version='0.5',
    license='MIT',
    author='Skynse',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=setuptools.find_packages(),
    include_package_data=True,
    author_email='',
    description='Easy API-less reddit scraper',
    python_requires='>=3.6',
)
