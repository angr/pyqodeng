import pytest
from pyqode.core.widgets import RecentFilesManager, MenuRecentFiles


def test_open_file():
    manager = RecentFilesManager('pyQode', 'test')
    manager.clear()
    with pytest.raises(IndexError):
        manager.last_file()
    manager.open_file(__file__)
    assert len(manager.get_recent_files()) == 1
    assert manager.last_file() == __file__


def test_remove_file():
    manager = RecentFilesManager('pyQode', 'test')
    manager.max_recent_files = 10
    manager.clear()
    manager.open_file(__file__)
    manager.open_file(pytest.__file__)
    assert manager.last_file() == pytest.__file__
    manager.remove(pytest.__file__)
    assert len(manager.get_recent_files()) == 1
    assert manager.last_file() == __file__


def test_max_files():
    manager = RecentFilesManager('pyQode', 'test')
    manager.clear()
    manager.max_recent_files = 1
    manager.open_file(__file__)
    assert manager.last_file() == __file__
    manager.open_file(pytest.__file__)
    assert manager.last_file() == pytest.__file__
    assert len(manager.get_recent_files()) == 1


def test_menu_recent_files():
    manager = RecentFilesManager('pyQode', 'test')
    manager.clear()
    manager.open_file(__file__)
    manager.open_file(pytest.__file__)
    mnu = MenuRecentFiles(None, recent_files_manager=manager, title='Recents',
                          icon_provider=None, clear_icon=None)
    mnu.show()


def test_normalized_path():
    manager = RecentFilesManager('pyQode', 'test')
    manager.clear()
    manager.open_file(r'c:\Test/test.cbl')
    manager.open_file(r'c:\Test\test.cbl')
    assert len(manager.get_value('list', [])) == 1
