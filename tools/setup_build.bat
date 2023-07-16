
rd /s /q build
rd /s /q dist
rd /s /q PlistParser.egg-info

@echo
python setup.py sdist --formats=gztar bdist_wheel build_ext --verbose



@REM tar -zcvf ./dist/PlistParser.doc-info.tar.gz PlistParser.doc-info
@REM tar -zcvf ./dist/PlistParser.test-s.tar.gz PlistParser.test-s

