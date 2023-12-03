import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dateiname",default='nicht angegeben')
args = parser.parse_args()
print(args.dateiname)