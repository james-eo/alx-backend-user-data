
# 0x00. Personal Data

This `README.md` file contains all the necessary details about the project, including resources, learning objectives, requirements, and tasks. Each task is explained, and code snippets are provided for clarity.

## Back-end Authentication

### Resources
Read or watch:
- [What Is PII, non-PII, and Personal Data?](https://example.com)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://example.com)

### Learning Objectives
At the end of this project, you should be able to explain the following concepts without using Google:
- Examples of Personally Identifiable Information (PII)
- How to implement a log filter that will obfuscate PII fields
- How to encrypt a password and check the validity of an input password
- How to authenticate to a database using environment variables

### Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be meaningful sentences explaining the purpose of the module, class, or method
- All your functions should be type-annotated

### Tasks

#### 0. Regex-ing
Write a function called `filter_datum` that returns the log message obfuscated:

- **Arguments**:
  - `fields`: a list of strings representing all fields to obfuscate
  - `redaction`: a string representing by what the field will be obfuscated
  - `message`: a string representing the log line
  - `separator`: a string representing which character is separating all fields in the log line (`message`)
- The function should use a regex to replace occurrences of certain field values.
- `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.

**Example**:
```python
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

