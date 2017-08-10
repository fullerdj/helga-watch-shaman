from setuptools import setup, find_packages

version = '0.0.1'

setup(name="helga_watch_shaman",
      version=version,
      description=('helga plugin to watch Shaman builds'),
      classifiers=['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
      keywords='irc bot',
      author='Douglas Fuller',
      author_email='douglas.fuller@gmail.com',
      url='https://github.com/fullerdj/helga-watch-shaman',
      license='MIT',
      packages=find_packages(),
      py_modules=['helga_watch_shaman'],
      install_requires=[
      ],
      entry_points = dict(
          helga_plugins = [
              'helga_watch_shaman = helga_watch_shaman:helga_watch_shaman',
          ],
      ),
)
