from distutils.core import setup

setup(
    name='Panku',
    scripts=['Panku/panku'],
    version='0.1',
    packages=['Panku'],
    license='MIT',
    author='Skynse',
    package_data={'': ['./requirements.txt']},
    include_package_data=True,
    author_email='',
    description='Easy API-less reddit scraper'\
)
