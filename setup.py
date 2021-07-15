import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as version_file:
    version = version_file.read().strip()

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setuptools.setup(
    name='uvvispy',
    version=version,
    description='Package for handling optical absorption data.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Till Biskup',
    author_email='till@till-biskup.de',
    url='https://www.uvvispy.de/',
    project_urls={
        'Documentation': 'https://docs.uvvispy.de/',
        'Source': 'https://github.com/tillbiskup/uvvispy',
    },
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    keywords=[
        "spectroscopy",
        "optical spectroscopy",
        "UV-visible spectroscopy",
        "uvvis",
        "data processing and analysis",
        "reproducible science",
        "reproducible research",
        "good scientific practice",
        "recipe-driven data analysis",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=[
        'aspecd>=0.2.2',
    ],
    extras_require={
        'dev': ['prospector'],
        'docs': ['sphinx', 'sphinx-rtd-theme'],
    },
    python_requires='>=3.5',
)
