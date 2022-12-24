This is a very simple example package used as part of the UCL
[Research Software Engineering with Python](development.rc.ucl.ac.uk/training/engineering) course.

## Installation

```bash
pip install git+git://github.com/ucl-rits/greeter
pip install git+git://github.com/chongfengling/sagittal_average_packaging
```

## Usage
    
Invoke the tool with `sagittal_average_run <file_input> <file_output>` or use it on your own library:

```python
from Sagittal_Average import sagittal_brain

sagittal_brain.run_averages(file_input, file_output)
```