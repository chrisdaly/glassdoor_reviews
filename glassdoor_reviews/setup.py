from setuptools import setup

setup(name='glassdoor_reviews',
      version='0.1',
      description="Extracts all reviews on a given company's glassdoor page.",
      url='https://github.com/chrisdaly/glassdoor-reviews',
      author='Chris Daly',
      author_email='chrisdaly1988@gmail.com',
      license='MIT',
      packages=['glassdoor_reviews'],
      install_requires=['requests', 'pandas', 'bs4', 'lxml'],
      zip_safe=False)