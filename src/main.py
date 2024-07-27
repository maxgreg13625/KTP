from utility import MY_AES
from utility import get_config, export_config

def main():
    config = get_config()
    aes = MY_AES(config['Required']['key'])
    print(config['Required']['key'])

    for kv in config.items('KeyValue'):
        print(f'{kv[0]}, {kv[1]}')
        config['KeyValue'][kv[0]] = aes.encrypt(kv[1])
        print(f"{kv[0]}, {config['KeyValue'][kv[0]]}")
        export_config(config)

    new_config = get_config('./setting/encrypt_config.ini')
    pass

if __name__ == '__main__':
    main()