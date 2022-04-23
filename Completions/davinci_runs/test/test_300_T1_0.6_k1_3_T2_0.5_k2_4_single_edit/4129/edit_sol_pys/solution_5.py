#!/bin/bash

# author: TheUnnamedDude
# source: https://github.com/TheUnnamedDude/wifi-hotspot/blob/master/wifi-hotspot.sh

# check if root
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root"
	exit 1
fi

# check if wlan0 is available
if [[ -z $(ifconfig | grep wlan0) ]]; then
	echo "wlan0 not found"
	exit 1
fi

# check if network-manager is available
if [[ -z $(which network-manager) ]]; then
	echo "network-manager not found"
	exit 1
fi

# check if nmcli is available
if [[ -z $(which nmcli) ]]; then
	echo "nmcli not found"
	exit 1
fi

# check if hostapd is available
if [[ -z $(which hostapd) ]]; then
	echo "hostapd not found"
	exit 1
fi

# check if dnsmasq is available
if [[ -z $(which dnsmasq) ]]; then
	echo "dnsmasq not found"
	exit 1
fi

# check if iptables is available
if [[ -z $(which iptables) ]]; then
	echo "iptables not found"
	exit 1
fi

# check if dnsmasq is installed
if [[ -z $(dpkg-query -W -f='${Status}' dnsmasq 2>/dev/null | grep "ok installed") ]]; then
	echo "dnsmasq not installed"
	exit 1
fi

# check if hostapd is installed
if [[ -z $(dpkg-query -W -f='${Status}' hostapd 2>/dev/null | grep "ok installed") ]]; then
	echo "hostapd not installed"
	exit 1
fi

# check if network-manager is installed
if [[ -z $(dpkg-query -W -f='${Status}' network-manager 2>/dev/null | grep "ok installed") ]]; then
	echo "network-manager not installed"
	exit 1
fi

# check if nmcli is installed
if [[ -z $(dpkg-query -W -f='${Status}' nmcli 2>/dev/null | grep "ok installed") ]]; then
	echo "nmcli not installed"
	exit 1
fi

# check if iptables is installed
if [[ -z $(dpkg-query -W -f='${Status}' iptables 2>/dev/null | grep "ok installed") ]]; then
	echo "iptables not installed"
	exit 1
fi

# check if a hotspot is already active
if [[ -z $(nmcli -t -f active con show --active | grep hotspot) ]]; then
	echo "hotspot already active"
	exit 1
fi

# get the interface name
read -p "Enter the interface name: " interface

# get the hotspot name
read -p "Enter the hotspot name: " hotspot_name

# get the hotspot password
read -p "Enter the hotspot password: " hotspot_password

# get the hotspot channel
read -p "Enter the hotspot channel: " hotspot_channel

# get the hotspot ip
read -p "Enter the hotspot ip: " hotspot_ip

# get the dhcp start ip
read -p "Enter the dhcp start ip: " dhcp_start_ip

# get the dhcp end ip
read -p "Enter the dhcp end ip: " dhcp_end_ip

# get the dhcp lease time
read -p "Enter the dhcp lease time: " dhcp_lease_time

# create the hotspot
nmcli device wifi hotspot ifname "$interface" ssid "$hotspot_name" password "$hotspot_password" channel "$hotspot_channel"

# configure the hotspot ip
nmcli con modify hotspot ipv4.addresses "$hotspot_ip/24"

# configure the dhcp ip range
nmcli con modify hotspot ipv4.dhcp-range "$dhcp_start_ip,$dhcp_end_ip,$dhcp_lease_time"

# configure the dhcp options
nmcli con modify hotspot ipv4.dhcp-options "3,$hotspot_ip"

# configure the dns
nmcli con modify hotspot ipv4.dns "8.8.8.8,8.8.4.4"

# configure the dns search
nmcli con modify hotspot ipv4.dns-search ""

# restart the hotspot
nmcli con down hotspot && nmcli con up hotspot

# configure the iptables
iptables -t nat -A POSTROUTING -o enp0s25 -j MASQUERADE
iptables -A FORWARD -i enp0s25 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i wlan0 -o enp0s25 -j ACCEPT
