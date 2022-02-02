import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="peter-parquet",
    version='0.2.0',
    author="Rafael Silva",
    author_email="rafaelsilva@posteo.net",
    description="Quiclky inspect parquet files in command line",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sjlva/peter-parquet",
    py_modules=['view_parquet'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'click==8.0.3',
        'pyarrow==6.0.1',
        'pandas==1.4.0',
        'rich_dataframe==0.2.0'
    ],
    entry_points='''
        [console_scripts]
        view_parquet=view_parquet:main
    ''',
)
