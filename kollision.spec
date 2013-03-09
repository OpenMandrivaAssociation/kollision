Name:		kollision
Version:	4.10.1
Release:	1
Epoch:		1
Summary:	A simple ball dodging game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kollision/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description -n kollision
A simple ball dodging game.

%files
%{_kde_bindir}/kollision
%{_kde_applicationsdir}/kollision.desktop
%{_kde_appsdir}/kollision
%{_kde_iconsdir}/*/*/apps/kollision.*
%{_kde_docdir}/*/*/kollision

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

