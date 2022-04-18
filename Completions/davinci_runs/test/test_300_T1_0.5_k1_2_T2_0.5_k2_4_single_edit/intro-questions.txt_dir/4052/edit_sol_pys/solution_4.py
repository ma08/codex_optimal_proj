#!/bin/bash

# 
# This file originates from Kite's Circuit Sword control board project.
# Author: Kite (Giles Burgess)
# 
# THIS HEADER MUST REMAIN WITH THIS FILE AT ALL TIMES
#
# This firmware is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This firmware is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this repo. If not, see <http://www.gnu.org/licenses/>.
#

#
# This file handles the creation of a new 'config' file on the SD card.
# It will prompt the user for the name of the new config, and then copy
# the 'default' config to the new config, renaming it in the process.
#

#
# This script is called from 'config_menu.sh'
#

# Get the name of the new config
echo "Enter the name of the new config:"
read new_config_name

# Copy the 'default' config to the new config name
cp /storage/.config/default /storage/.config/$new_config_name

# Let the user know we're done
echo "New config '$new_config_name' created!"

# Wait a few seconds...
sleep 2

# Exit back to 'config_menu.sh'
exit
