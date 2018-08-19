from distutils.core import setup

setup(
    name='crypto_tool',
    description='Crypto History is a tool for collecting day by '
                'day history for the most popular crypto currencies.',
    version='0.1dev',
    packages=['crypto_history', ],
    author='Gavrilo Andric',
    author_email='gavriloandric@gmail.com',
    license='MIT License',
    long_description=open('README.md').read(),
)
