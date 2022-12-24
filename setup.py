from setuptools import setup, find_packages

setup(
    name="Sagittal_Average",
    version="0.1.2",
    packages=find_packages(),
    entry_points={
        'console_scripts':['sagittal_average_run = Sagittal_Average.command:process']
    }
)