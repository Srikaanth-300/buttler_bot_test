import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse multiple integers.")
    parser.add_argument('--tableno', type=int, nargs='+', required=True, help='A list of integer numbers')
    
    args = parser.parse_args()
    order = {args.tableno}
    #print(f'The provided integers are: {args.tableno[2]}')
    print(order)

if __name__ == '__main__':
    main()
