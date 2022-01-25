from TemporaryStorage import TemporaryStorageInstance


def main():
    storage = TemporaryStorageInstance()
    print(storage.__create_providers_list__())
    print(storage.upload(input('Enter path to file: ')).url)


if __name__ == '__main__':
    main()
