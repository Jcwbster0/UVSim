import pytest
from _pytest import monkeypatch

from FileManager import FileManager

def test_openFile_returns_error_when_file_is_not_txt(monkeypatch):
    manager = FileManager()

    def fake_promptForFile():
        return "program.docx"

    monkeypatch.setattr(manager, "promptForFile", fake_promptForFile)

    result = manager.openFile()

    assert result == ([], "Error: .txt file expected")

def test_openFile_returns_lines_and_filename_for_valid_file(tmp_path, monkeypatch):
    manager = FileManager()

    test_file = tmp_path / "program.txt"
    test_file.write_text("+1007\n+2007\n+4300\n")

    def fake_promptForFile():
        return str(test_file)

    monkeypatch.setattr(manager, "promptForFile", fake_promptForFile)

    result = manager.openFile()

    assert result == (["+1007", "+2007", "+4300"], "program.txt")

def test_openFile_raises_error_if_file_does_not_exist(monkeypatch):
    manager = FileManager()

    def fake_promptForFile():
        return "nonexistent.txt"

    monkeypatch.setattr(manager, "promptForFile", fake_promptForFile)

    with pytest.raises(FileNotFoundError):
        manager.openFile()

def test_openFile_returns_lines_and_filename_for_valid_file(tmp_path, monkeypatch):
    manager = FileManager()

    test_file = tmp_path / "program.txt"
    test_file.write_text("+1007\n+2007\n+4300\n")

    def fake_promptForFile():
        return str(test_file)

    monkeypatch.setattr(manager, "promptForFile", fake_promptForFile)

    result = manager.openFile()

    assert result == (["+1007", "+2007", "+4300"], "program.txt")

def test_validateFile_returns_0_for_valid_file():
    manager = FileManager()
    lines = ["+1007", "+2007", "+4300"]

    result = manager.validateFile(lines)

    assert result == 0

def test_validateFile_returns_1_when_missing_halt():
    manager = FileManager()
    lines = ["+1007", "+2007", "+3007"]

    result = manager.validateFile(lines)

    assert result == 1

def test_validateFile_returns_2_when_opcodes_are_invalid():
    manager = FileManager()
    lines = ["+1007", "+6041", "+3407"]

    result = manager.validateFile(lines)

    assert result == 2

def test_validateFile_returns_2_for_line_with_wrong_length():
    manager = FileManager()
    lines = ["+1007", "+430"]

    result = manager.validateFile(lines)

    assert result == 2

def test_validateFile_returns_2_for_line_without_sign():
    manager = FileManager()
    lines = ["10007", "+4300"]

    result = manager.validateFile(lines)

    assert result == 2

def test_validateFile_returns_3_when_file_has_more_than_100_lines():
    manager = FileManager()
    lines = ["+1007" for _ in range(101)]

    result = manager.validateFile(lines)

    assert result == 3
