from pathlib import Path
from sync_other_try import sync
from tempfile import mkdtemp

def test_file_exist_in_source_no_in_destination():
    #source_path = mkdtemp()
    #destination_path = mkdtemp()
    #s_p = (Path(source_path)/'file.txt').write_text('Text for file')
    #result = sync(source_path, destination_path)
    #assert result[0] == 'COPY'
    source = {'hash1':'fn1'}
    destination = {}
    expectect = {['COPY', 'dest1/fn1','dest2/fn1']}
    result = sync(source,destination)
    assert result == expectect


def test_file_dont_exist_source_yes_destination():
    #source_path = mkdtemp()
    source = {}
    destination = {'hash1':'fn1'}
    #destination_path = source_path
    #s_p = (Path(destination_path)/'file.txt').write_text('Text for file')
    result = sync(source, destination)
    expectect = {['REMOVE', '','']}
    assert result == expectect

def test_file_exist_destination_different_dir():
    source_path = mkdtemp()
    destination_path = source_path
    s_p = (Path(destination_path)/'file.txt').write_text('Text for file')
    result = sync(source_path, destination_path)
    assert result[0] == 'MOVE'

def test_choise_the_same_dir():
    source_path = mkdtemp()
    destination_path = source_path
    s_p = (Path(source_path)/'file.txt').write_text('Text for file')
    result = sync(source_path, source_path)
    assert result[0] == 'NOTHING'

def test_file_different_name():
    source_path = mkdtemp()
    destination_path = source_path
    s_p = (Path(destination_path)/'file.txt').write_text('Text for file')
    result = sync(source_path, destination_path)
    new_name = 'file_new_name.txt'
    assert result[0] == 'RENAME'