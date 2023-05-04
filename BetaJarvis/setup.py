# from setuptools import setup, find_namespace_packages

# setup(name='BetaJarvis',
#       version='0.1',
#       description='BetaJarvis is a console assistant, who is able to manage contacts, notes and sort files on your PC. He can also bend disc C into a pretzel and bake it in the oven, so be aware.',
#       packages=find_namespace_packages(),#('BetaJarvis'),
#       #package_dir={'': 'BetaJarvis'},
#       entry_points={'console_scripts': ['jarvis = BetaJarvis.BetaJarvis']})


# from setuptools import setup, find_packages

# setup(
#       name='BetaJarvis',
#       version='0.1',
#       packages=find_packages('BetaJarvis'),
#       package_dir={'': 'BetaJarvis'},
#       #packages=find_packages(),
#       #include_package_data=True,
#       entry_points={'console_scripts': ['jarvis = BetaJarvis:main']})


from setuptools import setup, find_namespace_packages

setup(name='BetaJarvis',
      version='1.0',
      description='BetaJarvis is a console assistant, who is able to manage contacts, notes and sort files on your PC. He can also bend disc C into a pretzel and bake it in the oven, so be aware.',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['jarvis = BetaJarvis.BetaJarvis']})
      # entry_points={'console_scripts': ['helper = helper_2.helper_2']})