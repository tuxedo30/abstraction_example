from sync import compare_paths, select_paths

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
    file.add(source)
    compare_result = compare_paths(source, destination)
    is_copy_file = next(b for b in compare_result)
    assert compare_result 


def test_file_diferent_name():
    pass

def test_fileexist_destination_but_not_source():
    pass