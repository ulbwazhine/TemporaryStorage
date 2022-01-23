<div align="center">
  <h1>TempStorage</h1>
  <p>
    <img src="https://img.shields.io/pypi/dm/TempStorage">
    <img src="https://img.shields.io/pypi/v/TempStorage?label=version">
    <img src="https://img.shields.io/pypi/l/TempStorage">
    <img src="https://img.shields.io/github/repo-size/ulbwazhine/TempStorage">
  </p>
  <p>A simple library for temporary storage of small files.</p>
</div>

## Navigation
* [Install](https://github.com/ulbwazhine/TempStorage#install)
* [Usage](https://github.com/ulbwazhine/TempStorage#usage)
  * [In Python console](https://github.com/ulbwazhine/TempStorage#in-python-console)
  * [As a standalone application](https://github.com/ulbwazhine/TempStorage#as-a-standalone-application)
* [List of supported providers](https://github.com/ulbwazhine/TempStorage#list-of-supported-providers)
* [Links](https://github.com/ulbwazhine/TempStorage#links)

## Install
```
$ python -m pip install TempStorage
```

## Usage

#### In Python console:

```python
from TempStorage import TempStorageInstance

storage = TempStorageInstance()

storage.upload('/path/to/file')
```

```
>>> https://path/to/uploaded/file
```

#### As a standalone application:
```
$ python -m TempStorage
```

## List of supported providers

Full list of all currently supported providers

* [0x0.st](http://0x0.st) [up to 512 MB]
* [cockfile](https://cockfile.com) [up to 2048 MB]
* [FileDitch](https://fileditch.com) [up to 15360 MB]
* [oshi.at](https://oshi.at) [up to 5000 MB]
* [pomf.lain.la](https://pomf.lain.la) [up to 512 MB]
* [qu.ax](https://qu.ax) [up to 100 MB]
* [transfer.sh](https://transfer.sh) [up to 15360 MB]
* [uguu.se](https://uguu.se) [up to 100 MB]
* [x0.at](https://x0.at) [up to 1024 MB]

You can help the project by adding support for new providers by contributing on [GitHub](https://github.com/ulbwazhine/TempStorage).

## Links
* [Author](https://ulbwa.github.io)
* [GitHub](https://github.com/ulbwazhine/TempStorage)
* [PyPI](https://pypi.org/project/TempStorage)
* [Donate](https://ulbwa.github.io/go?to=donate)

