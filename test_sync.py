from sync import compare_paths, select_paths, copy_files, eliminate_files, rename_files
from unittest import assertFalse
import os


def test_selecting_diferent_paths():
    source, destination = select_paths()
    assert source != destination

def test_compare_paths():
    pass

def test_selecting_same_path():
    pass

def test_file_exist_source_but_not_destination():
    source = list()
    file = 'file_in_source.txt'
    file.add(source)
    destination = list()
    #file.add(source)
    compare_result = compare_paths(source, destination)
    #is_copy_file = next(b for b in compare_result if 'file_in_source.txt')
    assert not compare_result
    copy_files(source, destination)
    compare_result_after_copy = compare_paths(source, destination)
    assert compare_result_after_copy


def test_same_file_diferent_name():
    source = list()
    file = 'file_in_source.txt'
    Function = open(file, 'w') 
    Function.write("Test same content, diferent name") 
    Function.close() 
    file.add(source)
    destination = list()
    new_file_name = 'file_in_destination_diferent_name.txt'
    os.rename(file,new_file_name)
    new_file_name.add(destination)
    compare_result = compare_paths(source, destination)
    #is_copy_file = next(b for b in compare_result if 'file_in_source.txt')
    assert not compare_result
    rename_files(source, destination)
    compare_result_after_rename = compare_paths(source, destination)
    assert compare_result_after_rename

def test_file_exist_destination_but_not_source():
    source = list()
    file = 'file_in_source.txt'
    #file.add(source)
    destination = list()
    file.add(destination)
    compare_result = compare_paths(source, destination)
    #is_copy_file = next(b for b in compare_result if 'file_in_source.txt')
    assert not compare_result
    eliminate_files(source, destination)
    compare_result_after_delete = compare_paths(source, destination)
    assert compare_result_after_delete
    