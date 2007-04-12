Name:		crack-attack-music
Summary:	Music files for crack-attack
Version:	1
Release: 	3mdk
Url:		http://www.miguev.net/misc/
Source0:	%{name}.tar.bz2
Group:		Games/Arcade
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	crack-attack >= 1.1.10-5mdk
BuildArch:	noarch

%description
'Crack Attack!' is a free OpenGL game
based on the Super Nintendo classic Tetris Attack.

This package provides music to enhance the gaming experience.
%prep
%setup -q  -n data

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_gamesdatadir}/crack-attack/
cp -a music $RPM_BUILD_ROOT%{_gamesdatadir}/crack-attack/music

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_gamesdatadir}/crack-attack/music/

