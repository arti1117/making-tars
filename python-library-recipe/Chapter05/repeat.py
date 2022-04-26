import argparse

parser = argparse.ArgumentParser(description='Example command')

parser.add_argument('-s', '--string', type=str, help='string to display', required=True)
parser.add_argument('-n', '--num', type=int, help='number of times repeatedly display the string', default=2)

args = parser.parse_args()
print(args.string * args.num)
