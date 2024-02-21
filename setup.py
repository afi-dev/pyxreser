from setuptools import find_packages, setup

print('Build Pyxreser package...')

setup(
    name='pyxreser',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Pillow>=10.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pyxreser=pyxreser.app:main'
        ]
    },
    author='afi-dev',
    author_email='aconique@gmail.com',
    description='pyxreser is a small Python library designed to simplify the creation of Pyxel images by converting 256x256 pixel 15-color PNG or JPG images into .pyxres files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/afi-dev/pyxreser',
    license='LICENSE',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
    ],
    keywords="python pyxel pyxreser pyxres image converter color png jpg",
    project_urls={
        "Bug Reports": "https://github.com/afi-dev/pyxreser/issues",
        "Feature request": "https://github.com/afi-dev/pyxreser/issues",
        "Ko-fi": "https://ko-fi.com/afidev",
        "Buy me a coffee": "https://www.buymeacoffee.com/afidev",
        "Documentation": "https://github.com/afi-dev/pyxreser/blob/main/README.md",
        "Source": "https://github.com/afi-dev/pyxreser",
        "Changelog": "https://github.com/afi-dev/pyxreser/blob/main/CHANGELOG.md",
    },
    extras_require={},
    python_requires='>=3.0',
)
