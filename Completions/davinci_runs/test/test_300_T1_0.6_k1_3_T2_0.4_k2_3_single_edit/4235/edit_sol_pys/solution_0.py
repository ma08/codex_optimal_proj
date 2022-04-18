#!/bin/sh

#  file.sh
#  
#
#  Created by HSP SI Viet Nam on 5/15/14.
#
echo "Nhap ten file: "
read file
if [ -f $file ]
then
    echo "File $file ton tai"
else
    echo "File $file khong ton tai"
fi
