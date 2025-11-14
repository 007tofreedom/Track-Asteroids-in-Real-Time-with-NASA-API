from setuptools import setup, find_packages

setup(
    name='sentinel_satellite',  # The name of your package
    version='1.0.0',  # Version of your package
    packages=find_packages(),  # Automatically find packages in your repo
    py_modules=['satellite_animationv11'],  # Include your Python script
    install_requires=[
        'requests',
        'pygame',
        'colorama'
    ],  # Dependencies
    entry_points={
        'console_scripts': [
            'sentinel_satellite=satellite_animationv11:main',  # Command to run
        ],
    },
)
