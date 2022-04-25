
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2014 The Plaso Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the Google Drive log file parser."""
import __builtin__
import unittest
import os
import shutil
import tempfile
import time
import zipfile
# pylint: disable=unused-import
from plaso.formatters import googledrive as googledrive_formatter
from plaso.lib import event
from plaso.lib import eventdata
from plaso.lib import timelib
from plaso.parsers import googledrive
from plaso.parsers import test_lib
# pylint: enable=unused-import
from plaso.winnt import time_zones
import pytz
import datetime


class GoogleDriveTest(test_lib.ParserTestCase):
  """Tests for the Google Drive log file parser."""

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    self._parser = googledrive.GoogleDriveParser()
    self._time_zone = time_zones.TimeZone(
        time_zones.TIME_ZONES['US/Pacific'])
    self._timestamp = timelib.Timestamp.CopyFromString(
        '2013-11-04 00:00:00')
    self._timestamp_utc = timelib.Timestamp.CopyFromString(
        '2013-11-04 00:00:00')
    self._timestamp_utc = self._timestamp_utc.SetTimeZone(pytz.UTC)

  def testParse(self):
    """Tests the Parse function."""
    test_file = self._GetTestFilePath([u'Drive.log'])
    event_queue_consumer = self._ParseFile(self._parser, test_file)
    event_objects = self._GetEventObjectsFromQueue(event_queue_consumer)

    self.assertEqual(len(event_objects), 2)

    event_object = event_objects[0]

    expected_timestamp = timelib.Timestamp.CopyFromString(
        '2013-11-04 00:00:00')
    self.assertEqual(event_object.timestamp, expected_timestamp)

    self.assertEqual(event_object.timestamp_desc, 'Last Updated')

    expected_msg = (
        u'[{0:s}] '
        u'Version: 1.0.0.0 '
        u'AppName: Google Drive '
        u'AppVersion: 1.0.0.0 '
        u'Last Updated: 2013-11-04 00:00:00 '
        u'OS: Windows '
        u'OS Version: 6.1.7601 '
        u'Locale: en-US '
        u'User Name: John Doe '
        u'User Email: john@gmail.com '
        u'User Google ID: 1234567890').format(test_file)

    expected_msg_short = (
        u'[{0:s}] Version: 1.0.0.0 AppName: Google Drive '
        u'AppVersion: 1.0.0.0 Last Updated: 2013-11-04 00:00:00 OS: '
        u'Windows OS Version: 6.1.7601 Locale: en-US User Name: John Doe '
        u'User Email: john@gmail.com User Google ID: 1234567890').format(
            test_file)

    self._TestGetMessageStrings(event_object, expected_msg, expected_msg_short)

    event_object = event_objects[1]

    expected_timestamp = timelib.Timestamp.CopyFromString(
        '2013-11-04 00:00:00')
    self.assertEqual(event_object.timestamp, expected_timestamp)

    self.assertEqual(event_object.timestamp_desc, 'Last Updated')

    expected_msg = (
        u'[{0:s}] '
        u'Version: 1.0.0.0 '
        u'AppName: Google Drive '
        u'AppVersion: 1.0.0.0 '
        u'Last Updated: 2013-11-04 00:00:00 '
        u'OS: Windows '
        u'OS Version: 6.1.7601 '
        u'Locale: en-US '
        u'User Name: John Doe '
        u'User Email: john@gmail.com '
        u'User Google ID: 1234567890 '
        u'Sync Folder Path: C:\\GoogleDrive '
        u'Sync Folder ID: 0Bz9-sT1-sT1-sT1-sT1-sT1 '
        u'Sync Folder Title: Google Drive '
        u'Sync Folder Type: My Drive '
        u'Sync Enabled: True '
        u'Sync Paused: False '
        u'Sync Full Scan: False').format(test_file)

    expected_msg_short = (
        u'[{0:s}] Version: 1.0.0.0 AppName: Google Drive '
        u'AppVersion: 1.0.0.0 Last Updated: 2013-11-04 00:00:00 OS: '
        u'Windows OS Version: 6.1.7601 Locale: en-US User Name: John Doe '
        u'User Email: john@gmail.com User Google ID: 1234567890 '
        u'Sync Folder Path: C:\\GoogleDrive Sync Folder ID: '
        u'0Bz9-sT1-sT1-sT1-sT1-sT1 Sync Folder Title: Google Drive '
        u'Sync Folder Type: My Drive Sync Enabled: True Sync Paused: False '
        u'Sync Full Scan: False').format(test_file)

    self._TestGetMessageStrings(event_object, expected_msg, expected_msg_short)


if __name__ == '__main__':
  unittest.main()
