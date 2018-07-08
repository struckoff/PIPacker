from packager import download_package, pack

import pytest
import os

class TestDownload_package:
    package = 'requests'
    result = download_package(package, 'packages')
    def test_resulr_is_valid_path(self):
        assert(self.result == f'packages{os.sep}{self.package}')
    def test_result_is_a_dir(self):
        assert(os.path.isdir(self.result))
    def test_resuslt_dir_not_empty(self):
        assert(len(os.listdir(self.result)) > 0)

class TestPack:
    package = 'requests'
    download_source = download_package(package, 'packages')
    result = pack(package, download_source)
    def test_result_is_valid_path(self):
        assert(self.result == f'{os.getcwd()}{os.sep}{self.download_source}.zip')
    def test_is_file(self):
        assert(os.path.isfile(self.result))