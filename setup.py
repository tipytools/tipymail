from setuptools import setup, find_packages

setup(
    name='tipymail',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'markdown',
    ],
    test_suite='tests',
    tests_require=[
        'unittest',
    ],
    author='Mauly dotDev',
    author_email='mauly.dev@gmail.com',
    description='A Python package for sending HTML or Markdown formatted emails securely.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tipytools/tipymail',
    license='MIT',
)
