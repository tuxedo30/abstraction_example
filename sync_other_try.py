from curses import has_extended_color_support
import hashlib
from importlib.metadata import files
import os
from pathlib import Path

def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(65536)
        while buf:
            hasher.update(buf)
            buf = file.read(65536)
    return hasher.hexdigest()

def get_list_hashes_source(sourcer_path):
    source_hashes = {}
    for folder,_,files in os.walk(sourcer_path):
        for fn in files:
            path = Path(folder)/fn
            hashing= hash_file(path)
            source_hashes[Path(folder)/fn] = hashing
    return source_hashes

def get_list_hashes_destination(destination_path):
    destination_hashes= set()
    for forlder,_,files in os.walk(destination_path):
        for fn in files:
            dest_path=Path(forlder)/fn
            dest_hash = hash_file(dest_path)
            destination_hashes.add(dest_hash)
    return destination_hashes

def define_action(source, source_hashes,destination, destination_hashes):
    action_list = {}
    

    return action_list