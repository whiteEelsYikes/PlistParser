
rd /s /q build
rd /s /q dist
rd /s /q PlistParser.egg-info


python setup.py sdist --formats=gztar bdist_wheel



