from setuptools import setup
setup(
  name = 'view-my-photos',
  py_modules=['app'],
  version = '1.0.2',
  python_requires='>3.6',
  description = 'Generates an HTML gallery of photos indicating the folder where they are stored.',
  author = 'Andros Fenollosa',
  author_email = 'andros@fenollosa.email',
  url = 'https://github.com/tanrax/view-my-photos',
  keywords = ['photos', 'terminal', 'console', 'html', 'css'],
  classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ),
  install_requires=[
      'Click>=7.0',
      'pillow'
  ],
  entry_points='''
      [console_scripts]
      view-my-photos=app:main
  '''
)
