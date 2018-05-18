#coding:utf-8

try:  # pip <= 9.0
    from pip.req import parse_requirements
except ImportError: # pip >= 10
    from pip._internal.req import parse_requirements


from setuptools import (
    find_packages,
    setup,
)


with open('./VERSION.txt', 'rb') as f:
    version = f.read().strip()
    """
        作为一个合格的模块，应该要有版本号哦。
    """
setup(
    name='scrapy_plus',    # 模块名称
    version=version,
    description='A mini spider framework, like Scrapy',    # 描述
    packages=find_packages(exclude=[]),
    author='Heima Python7',
    author_email='your@email.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='http://www.treenewbee.com/',
    install_requires=[str(ir.req) for ir in parse_requirements("requirements.txt", session=False)],#所需的运行环境
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
