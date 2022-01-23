from TempStorage import TempStorageInstance


def main():
    storage = TempStorageInstance()
    print(storage.upload(input('Enter path to file: ')).url)


if __name__ == '__main__':
    main()
