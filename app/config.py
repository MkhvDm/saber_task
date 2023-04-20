import os

# opt. get variables from .env

ROOT_DIR = os.getcwd()
BUILDS_DIR = 'builds'
BUILDS_YAML_FILE = 'builds.yaml'
TASKS_YAML_FILE = 'tasks.yaml'
BUILDS_YAML_ABSPATH = os.path.join(ROOT_DIR, BUILDS_DIR, BUILDS_YAML_FILE)
TASKS_YAML_ABSPATH = os.path.join(ROOT_DIR, BUILDS_DIR, TASKS_YAML_FILE)

HOST = '0.0.0.0'
PORT = 8000
