'''
Our main test file which we will use to plan our features before we implement them.
'''

from pathlib import Path

from src.main import main


def test_main():
    '''
    Test to ensure that the main.py file exists in the src directory.
    '''
    assert Path(
        "src/main.py").exists(), "The main.py file should exist in the src directory."


def test_main_function():
    '''
    Test to ensure that the main function is defined in main.py.
    '''
    assert callable(
        main), "The main function should be defined and callable in main.py."


def test_main_function_completes_successfully():
    '''
    Test that main function completes without raising exceptions.
    '''
    # This will automatically fail if any exception is raised
    main()
