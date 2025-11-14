from setuptools import setup, find_packages

setup(
    name='sentinel-satellite',
    version='0.1.0',
    description='Terminal-based spy satellite simulation with ASCII art and real-time controls, integrated with NASA API for live asteroid events.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='007tofreedom',
    author_email='micahramos59@gmail.com',
    url='https://github.com/007tofreedom/Track-Asteroids-in-Real-Time-with-NASA-API',
    packages=find_packages(),
    install_requires=[
        # List your requirements here, for example: 'requests>=2.25'
    ],
    entry_points={
        'console_scripts': [
            'sentinel-satellite=main:main',  # Adjust 'main:main' if your entry point is elsewhere
        ],
    },
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
