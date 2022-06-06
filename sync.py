import io
import os
import string
from typing import List
from webbrowser import open_new
import hashlib
import shutil
from pathlib import Path

#This was should for test xd
#path_source = '/'
#path_destination = '/'

BLOCKSIZE = 65536

def hash_file(path):
    hasher = hashlib.sha1()
    with path.open("rb") as file:
        buf = file.read(BLOCKSIZE)
        while buf:
            hasher.update(buf)
            buf = file.read(BLOCKSIZE)
    return hasher.hexdigest()

def sync(source, dest): 
    source_hashes = {}
    for folder, _, files in os.walk(source):
        for fn in files:
            source_hashes[hash_file(Path(folder)/fn)] = fn
    seen = set()
    for forlder,_,files in os.walk(dest):
        for fn in files:
            dest_path=Path(forlder)/fn
            dest_hash = hash_file(dest_path)
            seen.add(dest_hash)
            if dest_hash not in source_hashes:
                dest_path.remove()
            elif dest_hash in source_hashes and fn != source_hashes[dest_hash]:
                shutil.move(dest_path, Path(folder)/source_hashes[dest_hash])
    for  src_hash, fn in source_hashes.items():
        if src_hash not in seen:
            shutil.copy(Path(source)/fn,Path(dest)/fn)



# def select_path_source():
#     return input('Please, enter the source path: ')


# def select_path_destination():
#     return input('Please, enter the destination path: ')


# def compare_paths(source: str, destination: str) -> bool:
#     list_source= os.listdir(source)
#     list_destination= os.listdir(destination)
    
#     file_exist=False
#     list_extra_destination = List()
#     list_extra_destination.extend(list_destination)

#     for file in list_source:
#         open_file = io.open(source +'/'+ file,'b')
#         file_read = open_file.io.read()

#         for comparation in list_destination:
#             open_comparation = io.open(destination +'/'+comparation, 'b')
#             comparation_read = open_comparation.io.read()
#             #Need: review the name, the data content, if nothing is found
            
#             if file_read == comparation_read:
                
#                 if open_file.name != open_comparation.name:
#                     os.rename(open_comparation.name, open_file.name)

#                 file_exist=True

#                 list_extra_destination.remove(comparation)

#         if file_exist == False:
#             #F*ck Windows xd
#             os.popen('cp '+ source+'/'+file+' '+destination)

#     for f in list_extra_destination:
#         os.remove(destination +'/'+f)

