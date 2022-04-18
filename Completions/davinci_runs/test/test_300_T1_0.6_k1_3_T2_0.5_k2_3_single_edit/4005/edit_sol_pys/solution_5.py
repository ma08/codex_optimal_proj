#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Class for handling files with data.
"""

import csv

class File():
    
    def __init__(self, name, mode='r'):
        """Constructor.
        
        Args:
            name: Name of the file.
            mode: Open mode.
        """
        
        self._name = name
        self._mode = mode
        self._file = None
        
    def open(self):
        """Open the file.
        """
        
        self._file = open(self._name, self._mode)
        
    def read(self):
        """Read the file.
        
        Returns:
            The file content.
        """
        
        return self._file.read()
        
    def read_csv(self, delimiter = '\t'):
        """Read the file as csv.
        
        Returns:
            The file content as csv.
        """
        
        return csv.reader(self._file, delimiter = delimiter)
        
    def write(self, data):
        """Write the data to the file.
        
        Args:
            data: Data to write.
        """
        
        self._file.write(data)
        
    def write_csv(self, data, delimiter = '\t'):
        """Write the data to the file as csv.
        
        Args:
            data: Data to write.
            delimiter: Delimiter to use.
        """
        
        writer = csv.writer(self._file, delimiter = delimiter)
        
        writer.writerows(data)
        
    def close(self):
        """Close the file.
        """
        
        self._file.close()
        
    def __enter__(self):
        """Enter the with statement.
        """
        
        self.open()
        
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the with statement.
        """
        
        self.close()
        
    def __del__(self):
        """Destructor.
        """
        
        self.close()
        
