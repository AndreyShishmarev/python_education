import shutil
import sys

shutil.copyfile('person.json', 'test_dir/person.json')

shutil.rmtree('test_dir')

sys.stdin  # standard input
sys.stdout  # standard output
sys.stderr  # standard output error

sys.exit(0)
