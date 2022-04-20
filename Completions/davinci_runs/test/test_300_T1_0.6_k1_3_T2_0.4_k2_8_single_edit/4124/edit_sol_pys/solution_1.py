#!/usr/bin/env python

#
#  Copyright (C) 2011-2014, 2016, 2018  Smithsonian Astrophysical Observatory
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#


import os
import sys
import glob
import shutil
import fnmatch

from sherpa.utils import SherpaTestCase
from sherpa.utils import SherpaTest


class test_file(SherpaTestCase):

    def setUp(self):
        self.datadir = os.path.join(os.path.dirname(__file__), 'tst')
        self.model = os.path.join(self.datadir, 'model.py')
        self.model_c = os.path.join(self.datadir, 'model.so')
        self.model_c_dir = os.path.join(self.datadir, 'model_dir')
        self.model_c_dir_file = os.path.join(self.model_c_dir, 'model.so')
        self.model_c_dir_file_py = os.path.join(self.model_c_dir, 'model.py')

    def tearDown(self):
        for f in glob.glob(os.path.join(self.datadir, '*.so')):
            os.remove(f)
        if os.path.exists(self.model_c_dir):
            shutil.rmtree(self.model_c_dir)

    @SherpaTest
    def test_load_model_py(self):
        self.assertFalse(os.path.exists(self.model_c))
        self.assertFalse(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.assertRaises(IOError, self.load_model, self.model_c)
        self.assertRaises(IOError, self.load_model, self.model_c_dir)

        self.load_model(self.model)
        self.assertFalse(os.path.exists(self.model_c))
        self.assertFalse(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir)
        self.assertFalse(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir_file)
        self.assertFalse(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir_file_py)
        self.assertFalse(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

    @SherpaTest
    def test_load_model_py_c(self):
        self.assertFalse(os.path.exists(self.model_c))
        self.assertFalse(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertFalse(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir_file)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model_c_dir_file_py)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

        self.load_model(self.model)
        self.assertTrue(os.path.exists(self.model_c))
        self.assertTrue(os.path.exists(self.model_c_dir_file))
        self.assertFalse(os.path.exists(self.model_c_dir_file_py))

if __name__ == '__main__':

    import sys
    if len(sys.argv) > 1:
        SherpaTest(sys.argv[1:]).test()
    else:
        SherpaTest().test()
