#!/bin/sh

# Gather information about the system
#
#

# Output file
OUTFILE="system.info"

# System information
echo "System information" > $OUTFILE
echo "------------------" >> $OUTFILE
echo "" >> $OUTFILE

# Hostname
echo "Hostname:" >> $OUTFILE
echo "---------" >> $OUTFILE
hostname >> $OUTFILE
echo "" >> $OUTFILE

# Kernel Version
echo "Kernel Version:" >> $OUTFILE
echo "---------------" >> $OUTFILE
uname -r >> $OUTFILE
echo "" >> $OUTFILE

# Uptime
echo "Uptime:" >> $OUTFILE
echo "-------" >> $OUTFILE
uptime >> $OUTFILE
echo "" >> $OUTFILE

# Last reboot
echo "Last Reboot:" >> $OUTFILE
echo "------------" >> $OUTFILE
who -b >> $OUTFILE
echo "" >> $OUTFILE

# CPU info
echo "CPU info:" >> $OUTFILE
echo "---------" >> $OUTFILE
cat /proc/cpuinfo | grep "model name" >> $OUTFILE
echo "" >> $OUTFILE

# RAM info
echo "RAM info:" >> $OUTFILE
echo "---------" >> $OUTFILE
free -m >> $OUTFILE
echo "" >> $OUTFILE

# Disk info
echo "Disk info:" >> $OUTFILE
echo "----------" >> $OUTFILE
df -h >> $OUTFILE
echo "" >> $OUTFILE

# Network info
echo "Network info:" >> $OUTFILE
echo "-------------" >> $OUTFILE
ip addr >> $OUTFILE
echo "" >> $OUTFILE

# Network connections
echo "Network connections:" >> $OUTFILE
echo "--------------------" >> $OUTFILE
netstat -tulpn >> $OUTFILE
echo "" >> $OUTFILE

# Active processes
echo "Active processes:" >> $OUTFILE
echo "-----------------" >> $OUTFILE
ps aux >> $OUTFILE
echo "" >> $OUTFILE
