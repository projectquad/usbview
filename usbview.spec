%define 	name	usbview
%define 	version	1.0
%define 	release	1
%define 	serial	1
%define 	prefix	/usr

Summary: 	USB topology and device viewer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/System
Url:		http://www.kroah.com/linux-usb/
Vendor:		Greg Kroah-Hartman <greg@kroah.com>
Source:		http://www.kroah.com/linux-usb/%{name}-%{version}.tar.gz
BuildRoot:	/var/tmp/%{name}-%{version}
Requires:	gtk+ >= 1.2.3

%description
USBView is a GTK program that displays the topography of the devices 
that are plugged into the USB bus on a Linux machine. It also displays 
information on each of the devices. This can be useful to determine if 
a device is working properly or not.

%prep
%setup -q

%build
./configure
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%doc ChangeLog COPYING* README TODO
%{prefix}/bin/usbview

%changelog
* Mon Dec 5 2000 Greg Kroah-Hartman <greg@kroah.com>
[usbview-1.0]
- fixed problem for devices that grabed more than one interface, the
  name of the device would show up repeated a bunch.  This was true
  for a lot of audio and video devices.
- Tweaked the configuration dialog a bit.
- Tweaked the about dialog a bit.
- Everything seems stable, so let's put a major number on this release.
- added a pixmap hacked up from an image by M G Berberich 
  <berberic@fmi.uni-passau.de> to the about screen
- cleaned up the spec file to hopefully build a bit better on different 
  versions of different distros.

* Sun Sep 10 2000 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.9.0]
- added Trond Eivind Glomsr�d's patch to always try to populate the
  device tree when the program is started.
- cleaned up the code layout, removing the i18n code for now. Also
  got rid of some old Glade helper code that was not being used. This
  reduced the tarball size by about 1/2!
- usbview now updates the device list when devices are plugged in or
  removed from the bus automatically (needs 2.4.0-test8 or later to
  work properly due to a patch I made for drivers/usb/inode.c to 
  enable this to work.)
- Made any device that does not have a driver associated with it, show
  up in red in the device listing.  This should help users with the
  problem that "My device shows up properly in usbview, but it isn't
  working," that a lot of people seem to have (it isn't obvious, I 
  know...)
- Added small, drab looking "About" dialog box, to make it easier to
  determine which version this is.

* Thu Jun 29 2000 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.8.1]
- fixed the Gtk-WARNING that happens the first time you press the
  [Refresh] button.
- sped up the device info display a bunch. Should work a lot better
  for devices that have a lot of interfaces and endpoints.
- fixed #ifdef bug in code. Thanks to Trond Eivind Glomsr�d for
  noticing this and providing a patch.
- fixed improper speed display for low speed devices. Thanks to
  Brad Hards for noticing this and prompting me to add support
  for high speed USB (like there will not be other changes for
  high speed when it happens...)

* Thu Jun 14 2000 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.8.0]
- Added ability to select where the devices file is located at.
  This allows you to view a usbdevfs devices file that comes
  from another user, for instance. It also accomidates those who
  do not mount usbdevfs at /proc/bus/usb.
- Fixed bug with devices that have a lot of interfaces.
- Changed the tree widget to a different style.
- Restructured the internal code a bit nicer (a lot of work to
  go with this...)
- Added a TODO file to the archive listing some potential changes
  that could be done.

* Tue Jan 4 2000 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.7.0]
- The logic for determining the name of the device changed to
  properly display the name of a keyboard or mouse when the
  HID driver is used. This is needed for kernel versions 2.3.36
  and up.

* Tue Dec 21 1999 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.6.0]
- now can handle multiple root hubs.
- added display of bus bandwidth information for root hubs.
- added support for device strings to describe the device.
- made logic for device name to be smarter due to the availability
  of the string descriptors.

* Tue Dec 7 1999 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.5.0]
- updated the parser to handle the fact that the interface now
  dictates what driver is loaded.
- Tested on kernel version 2.3.29

* Tue Oct 26 1999 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.4.0]
- redid the user interface slightly, making the tree always expanded,
  showing the top of the text field, and better balancing the splitter
  bar.
- changed the parsing to make it easier to handle any future changes
  in the way the format of /proc/bus/usb/devices

* Sun Oct 3 1999 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.2.0]
- Configuration, interface, and endpoint data is now displayed
  for each device.
- Fixed problem with processing the last line in the /proc/... file
  twice.

* Sat Oct 2 1999 Greg Kroah-Hartman <greg@kroah.com>
[usbview-0.1.0]
- devices are read from /proc/bus/usb/devices and put into a tree view
- very basic information is displayed about each device when it is
  selected

