from setuptools import setup

setup(name='glassdoor_reviews',
      version='0.1',
      description="Extracts all reviews on a given company's glassdoor page.",
      url='https://github.com/w2ogroup/Notebooks/tree/master/Glassdoor%20MReviews',
      author='Chris Daly',
      author_email='cdaly@w2ogroup.com',
      license='MIT',
      packages=['glassdoor_reviews'],
      install_requires=['requests', 'pandas', 'bs4', 'lxml'],
      zip_safe=False)