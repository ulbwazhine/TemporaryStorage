python setup.py sdist
twine upload dist/*
rm -rf "dist"
rm -rf "TemporaryStorage.egg-info"