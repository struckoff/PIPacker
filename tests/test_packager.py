from packager import download_package

import pytest
import os

class TestDownload_package:
    package = 'requests'
    result = download_package(package, 'packages')
    def test_resulr_valid(self):
        assert(self.result == f'packages{os.sep}{self.package}')
    def test_result_is_a_dir(self):
        assert(os.path.isdir(self.result))
    def test_resuslt_dir_not_empty(self):
        assert(len(os.listdir(self.result)) > 0)