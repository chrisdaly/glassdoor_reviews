from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='glassdoor_reviews',
      version='0.2',
      description="Extracts all reviews on a given company's glassdoor page.",
      long_description=readme(),
      url='https://github.com/w2ogroup/Notebooks/tree/master/Glassdoor%20MReviews',
      author='Chris Daly',
      author_email='cdaly@w2ogroup.com',
      license='MIT',
      packages=['glassdoor_reviews'],
      install_requires=['bs4'],  # 'lxml'
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
