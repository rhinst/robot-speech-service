from setuptools import setup, find_packages
import platform


setup(
  name='robot-speech-service',
  version='0.1',
  description='Robot speech service',
  url='https://github.com/rhinst/robot-speech-service',
  author='Rob Hinst',
  author_email='rob@hinst.net',
  license='MIT',
  packages=find_packages(),
  data_files=[
    ('config', ['config/default.yaml']),
    ('config/dev', ['config/dev/env.yaml.dist']),
  ],
  install_requires=[
    'redis==3.5.3',
    'himl==0.7.0',
    'gTTS==2.2.1',
    'pydub==0.24.1'
  ],
  test_suite='tests',
  tests_require=['pytest==6.2.1'],
  entry_points={
    'console_scripts': ['speech=speech.__main__:main']
  }
)