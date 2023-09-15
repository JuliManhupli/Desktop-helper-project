from setuptools import setup, find_namespace_packages

setup(name='yourhelper',
      version='0.0.4',
      description='YourHelper is a Python application that provides various tools and utilities in one place.',
      long_description=open("README.md", "r", encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      python_requires=">=3.10",
      classifiers=["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   ],
      url='https://github.com/JuliManhupli/YourHelper',
      author='Lambda Crew',
      author_email='juliamangup@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      install_requires=["requests==2.31.0", "tabulate==0.9.0", "gTTS==2.3.2", "playsound==1.2.2", "translate==3.6.1",
                        "pydub==0.25.1", "py7zr==0.20.6", "translators==5.8.3", "pyttsx3==2.90"],
      entry_points={'console_scripts': ['yourhelper=yourhelper.main:main']}
      )
