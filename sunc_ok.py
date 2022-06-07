from importlib.resources import path
import os 
from pathlib import Path
import hashlib
import shutil

def hash_file(file_path):
    hasher = hashlib.sha1()
    with file_path.open("rb") as file:
        buf = file.read(65536)
        while buf:
            hasher.update(buf)
            buf = file.read(65536)
    return hasher.hexadiges()

def read_path_and_hashes(root):
    hashes={}
    for folder, _, file in os.walk(root):
        for fn in file:
            hashes[hash_file(Path(folder)/fn)] = fn
    return hashes

def determine_actions(sh,dh,s,d):
    for sha, filename in sh.items():
        if sha not in dh:
            source_path = Path(s)/filename
            dest_path = Path(d)/filename
            yield 'COPY',source_path,dest_path
        elif dh[sha] != filename:
            old_path = Path(d)/dh[sha]
            new_path = Path(d)/filename
            yield 'MOVE', old_path, new_path
    for dha, filename in dh.items():
        if dha not in sh:
            yield 'DELETE', d/filename

def sync(source, dest):
    source_hashes = read_path_and_hashes(source)
    dest_hashes = read_path_and_hashes(dest)

    actions = determine_actions(source_hashes,dest_hashes,source, dest)

    for action, *paths in actions:
        if action == 'COPY':
            shutil.copyfile(*paths)
        if action == 'MOVE':
            shutil.move(*paths)
        if action == 'DELETE':
            os.remove(paths[0])