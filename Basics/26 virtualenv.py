'''
Virtual Environment in Python:
    We use virtual environments due to different projects support different Dependencies.
this is a complete isoloted environment of the original python and we can install dependencies
required by our own projects.

Done using the "venv" module

Usage:
1) python -m venv virtual_env_name_to_create (This will create a virtual_env in specified Destination)
2) Linux : source v_env_name/bin/activate
   Windows : v_env_name/scripts/activate.bat
3) pip install requirement dependencies (-r requirments.txt)
4) deactivate (To go out of virtual environment)
5) pip freeze (To show installed Dependencies)
6) pip freeze > requirements.txt (To save in text file)
'''