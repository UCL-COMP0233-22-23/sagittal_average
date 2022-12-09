from setuptools import setup, find_packages

setup(
    name="sagittal_average",  
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'sagittal_average_run = sagittal_average.command:process']}
)

#The name of the package above is NOT the name that you type when doing `import ...` 
#bc that name is the name of the folder which command.py is in ???