import os
import re
import json
from aocd import get_data

url_pattern = 'https://adventofcode.com/{year}/day/{day}/input'

def read_input(script_path, input_file='input.txt') -> str:
  cur_dir = os.path.dirname(script_path)
  file_path = os.path.join(cur_dir, input_file)

  if not os.path.exists(file_path):
    print('input file not found, downloading from aoc')
    download_input_from_online(script_path, input_file)

  return read_input_from_local(file_path)


def read_test_input(script_path, input_file='test_input.txt') -> str:
  cur_dir = os.path.dirname(script_path)
  file_path = os.path.join(cur_dir, input_file)

  return read_input_from_local(file_path)


def read_input_from_local(file_path: str) -> str:
  with open(file_path, 'r') as file:
    return file.read()


def download_input_from_online(script_path, input_file='input.txt'):
  cur_dir = os.path.dirname(script_path)
  year, day = get_year_day(script_path)
  session_id = get_session_id()

  try:
    data = get_data(session=session_id, day=int(day), year=year)
  except Exception as e:
    print(f"Failed to download file: {e}")
    return

  file_path = os.path.join(cur_dir, input_file)
  with open(file_path, 'wb') as file:
    file.write(data.encode('utf-8'))


def get_session_id() -> str:
  cur_dir = os.path.dirname(__file__)
  project_root = os.path.abspath(os.path.join(cur_dir, "../.."))
  credentails_path = os.path.join(project_root, 'credentials.json')
  with open(credentails_path) as json_file:
        items = json.load(json_file)
        return items['session_id']


def get_year_day(filepath: str) -> tuple:
  pattern = r"advent[-_]of[-_]code\/src\/(\d{4})\/(\d{2})"
  match = re.search(pattern, filepath)
  if match:
    year = match.group(1)
    day = match.group(2)
    return year, day
  else:
    print(f"file did not match to advent of code year/day: {filepath}")
    return None, None


def input_lines(input: str) -> list[str]:
  return input.splitlines(keepends=False)

