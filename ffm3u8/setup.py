import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ffm3u8',
    version='1.1.1',
    author='Nongyi,企鹅诶i',
    author_email='13360350080@163.com',
    description='A simple TS download module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Nong-Yi/ny.git',
    packages=["ffm3u8"],
    classifiers=[
        "programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT LICENSE",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

