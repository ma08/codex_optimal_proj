#!/usr/bin/perl
#
#  Copyright Statement:
#  --------------------
#  This software is protected by Copyright and the information contained
#  herein is confidential. The software may not be copied and the information
#  contained herein may not be used or disclosed except with the written
#  permission of MediaTek Inc. (C) 2006
#
#  BY OPENING THIS FILE, BUYER HEREBY UNEQUIVOCALLY ACKNOWLEDGES AND AGREES
#  THAT THE SOFTWARE/FIRMWARE AND ITS DOCUMENTATIONS ("MEDIATEK SOFTWARE")
#  RECEIVED FROM MEDIATEK AND/OR ITS REPRESENTATIVES ARE PROVIDED TO BUYER ON
#  AN "AS-IS" BASIS ONLY. MEDIATEK EXPRESSLY DISCLAIMS ANY AND ALL WARRANTIES,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT.
#  NEITHER DOES MEDIATEK PROVIDE ANY WARRANTY WHATSOEVER WITH RESPECT TO THE
#  SOFTWARE OF ANY THIRD PARTY WHICH MAY BE USED BY, INCORPORATED IN, OR
#  SUPPLIED WITH THE MEDIATEK SOFTWARE, AND BUYER AGREES TO LOOK ONLY TO SUCH
#  THIRD PARTY FOR ANY WARRANTY CLAIM RELATING THERETO. MEDIATEK SHALL ALSO
#  NOT BE RESPONSIBLE FOR ANY MEDIATEK SOFTWARE RELEASES MADE TO BUYER'S
#  SPECIFICATION OR TO CONFORM TO A PARTICULAR STANDARD OR OPEN FORUM.
#
#  BUYER'S SOLE AND EXCLUSIVE REMEDY AND MEDIATEK'S ENTIRE AND CUMULATIVE
#  LIABILITY WITH RESPECT TO THE MEDIATEK SOFTWARE RELEASED HEREUNDER WILL BE,
#  AT MEDIATEK'S OPTION, TO REVISE OR REPLACE THE MEDIATEK SOFTWARE AT ISSUE,
#  OR REFUND ANY SOFTWARE LICENSE FEES OR SERVICE CHARGE PAID BY BUYER TO
#  MEDIATEK FOR SUCH MEDIATEK SOFTWARE AT ISSUE.
#
#  THE TRANSACTION CONTEMPLATED HEREUNDER SHALL BE CONSTRUED IN ACCORDANCE
#  WITH THE LAWS OF THE STATE OF CALIFORNIA, USA, EXCLUDING ITS CONFLICT OF
#  LAWS PRINCIPLES.  ANY DISPUTES, CONTROVERSIES OR CLAIMS ARISING THEREOF AND
#  RELATED THERETO SHALL BE SETTLED BY ARBITRATION IN SAN FRANCISCO, CA, UNDER
#  THE RULES OF THE INTERNATIONAL CHAMBER OF COMMERCE (ICC).
#
#*****************************************************************************
#*
#* Filename:
#* ---------
#*   file.pl
#*
#* Project:
#* --------
#*
#*
#* Description:
#* ------------
#*   This script is used to parse file
#*
#* Author:
#* -------
#*   Qmei Yang (mtk03726)
#*
#****************************************************************************/

#****************************************************************************
# Included Modules
#****************************************************************************
use strict;
BEGIN { push @INC, '.\\tools\\' }  # add additional library path
use sysGenUtility;                 #pm file name without case sensitivity
use FileInfoParser;
use CommonUtility;
PrintDependModule();

#****************************************************************************
# Constants
#****************************************************************************
my $FILE_PM = "file.pm";
my $FILE_TXT = "file.txt";

#****************************************************************************
# Input Parameters and Global Variables
#****************************************************************************
my ($g_MAKEFILE, $g_BBFILE, $g_CUSTOMFILE, $g_PATH, $g_PROJECT, $g_PLATFORM, $g_FLAVOR, $g_MODE, $g_SCATTERFILE);
my ($g_MEMORYDUMPFILE, $g_MEMORYMAPFILE);
my ($g_MAKEFILE_ref, $g_BBFILE_ref, $g_CUSTOMFILE_ref);
my ($g_MAKEFILE_LIS_ref, $g_BBFILE_LIS_ref, $g_CUSTOMFILE_LIS_ref);

#****************************************************************************
# 1 >>> parse argments
#****************************************************************************
&FileInfo::ParseArgv($FILE_PM, \$g_MAKEFILE, \$g_BBFILE, \$g_CUSTOMFILE, \$g_PATH, \$g_PROJECT, \$g_PLATFORM, \$g_FLAVOR, \$g_MODE, \$g_SCATTERFILE, \$g_MEMORYDUMPFILE, \$g_MEMORYMAPFILE);

my $g_FOLDER_LIST_ref;
my $g_FILE_LIST_ref;
my $g_DUMMY_LIST_ref;
my $g_FILE_LIST_LIS_ref;

#****************************************************************************
# 2 >>> read file
#****************************************************************************
&FileInfo::ReadFile($g_MAKEFILE, $g_BBFILE, $g_CUSTOMFILE, $g_SCATTERFILE, $g_MEMORYDUMPFILE, $g_MEMORYMAPFILE, \$g_MAKEFILE_ref, \$g_BBFILE_ref, \$g_CUSTOMFILE_ref, \$g_MAKEFILE_LIS_ref, \$g_BBFILE_LIS_ref, \$g_CUSTOMFILE_LIS_ref);

#****************************************************************************
# 3 >>> parse file content
#****************************************************************************
&FileInfo::ParseFileContent($g_MAKEFILE_ref, $g_BBFILE_ref, $g_CUSTOMFILE_ref, $g_MAKEFILE_LIS_ref, $g_BBFILE_LIS_ref, $g_CUSTOMFILE_LIS_ref, \$g_FOLDER_LIST_ref, \$g_FILE_LIST_ref, \$g_DUMMY_LIST_ref, \$g_FILE_LIST_LIS_ref);

#****************************************************************************
# 4 >>> output file
#****************************************************************************
&FileInfo::OutputFile($g_FOLDER_LIST_ref, $g_FILE_LIST_ref, $g_DUMMY_LIST_ref, $g_FILE_LIST_LIS_ref);

#****************************************************************************
# 5 >>> generate file
#****************************************************************************
&FileInfo::GenFile($g_PATH, $g_PROJECT, $g_PLATFORM, $g_FLAVOR, $g_MODE, $g_FOLDER_LIST_ref, $g_FILE_LIST_ref, $g_DUMMY_LIST_ref, $g_FILE_LIST_LIS_ref);

#****************************************************************************
# oo >>>  Finished
#****************************************************************************
exit 0;
