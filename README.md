<div align="center">
  <h1>TemporaryStorage</h1>
  <p>
    <img src="https://img.shields.io/pypi/dm/TemporaryStorage">
    <img src="https://img.shields.io/pypi/v/TemporaryStorage?label=version">
    <img src="https://img.shields.io/pypi/l/TemporaryStorage">
    <img src="https://img.shields.io/github/repo-size/ulbwazhine/TemporaryStorage">
  </p>
  <p>A simple library for temporary storage of small files.</p>
</div>

## Navigation
* [Install](https://github.com/ulbwazhine/TemporaryStorage#install)
  * [Update](https://github.com/ulbwazhine/TemporaryStorage#update)
* [Usage](https://github.com/ulbwazhine/TemporaryStorage#usage)
  * [In Python console](https://github.com/ulbwazhine/TemporaryStorage#in-python-console)
  * [As a standalone application](https://github.com/ulbwazhine/TemporaryStorage#as-a-standalone-application)
* [List of supported providers](https://github.com/ulbwazhine/TemporaryStorage#list-of-supported-providers)
* [Links](https://github.com/ulbwazhine/TemporaryStorage#links)

## Warning
TemporaryStorage is not a platform for:

* Piracy
* Pornography and cruelty content
* Malware
* Storing personal information
* Anything illegal under Russian law

Using TemporaryStorage, you agree to the terms of [all listed resources](https://github.com/ulbwazhine/TemporaryStorage#list-of-supported-providers).

## Install
```
$ python3 -m pip install TemporaryStorage
```

### Update
```console
$ python3 -m pip install TemporaryStorage --upgrade
```

## Usage

#### In Python console:

```python
from TemporaryStorage import TemporaryStorageInstance

storage = TemporaryStorageInstance()

storage.upload('/path/to/file')
```

```
>>> https://path/to/uploaded/file
```

#### As a standalone application:
```
$ python -m TemporaryStorage
```

## List of supported providers

Full list of all currently supported providers:

| Provider | File size | Retention period |
| :---: | :---: | :---: |
| [0x0.st](http://0x0.st) | Up to 512 MB | From 30 to 365 days |
| [cockfile~](https://cockfile.com) | Up to 2048 MB | 2 days |
| [FileDitch](https://fileditch.com) | Up to 15360 MB | Unlimited |
| [oshi.at](https://oshi.at) | Up to 5000 MB | From 7 to 90 days |
| [pomf.lain.la](https://pomf.lain.la) | Up to 512 MB | Unlimited |
| [qu.ax](https://qu.ax) | Up to 100 MB | Unlimited |
| [Telegraph](https://telegra.ph) | Up to 50 MB | Unlimited |
| [transfer.sh](https://transfer.sh) | Unlimited | 14 days |
| [uguu.se](https://uguu.se) | Up to 100 MB | 2 days |
| [x0.at](https://x0.at) | Up to 1024 MB | From 10 to 360 days |

You can help the project by adding support for new providers by contributing on [GitHub](https://github.com/ulbwazhine/TemporaryStorage).

## Links
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/author.svg" height="30"/>](https://ulbwa.github.io)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/github.svg" height="30"/>](https://github.com/ulbwazhine/TemporaryStorage)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/pypi.svg" height="30"/>](https://pypi.org/project/TemporaryStorage)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/donate.svg" height="30"/>](https://ulbwa.github.io/go?to=donate)
