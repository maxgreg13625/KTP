from utility import get_config

def main():
    config = get_config()
    print(config['Required']['key'])

if __name__ == '__main__':
    main()