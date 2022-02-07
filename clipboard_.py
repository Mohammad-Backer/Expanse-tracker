import json
import sys
import clipboard


SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data

if __name__ == '__main__' :

    if (len(sys.argv)) == 2:
        data = load_data(SAVED_DATA)
        command = sys.argv[1]
        if command == 'save':
            key = input("Enter a key: ")
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
            print('data saved!')
        elif command == 'load':
            key = input("Enter a key: ")
            try:
                clipboard.copy(load_data(SAVED_DATA)[key])
                print('data copied to clipboard!')
            except:
                print('Key does not exist!')
        elif command == 'list':
            print(data)
        else:
            print('Unknown command')

    else:
        print("Please enter 1 command")
