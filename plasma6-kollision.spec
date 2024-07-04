#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name:		plasma6-kollision
Version:	24.05.2
Release:	%{?git:0.%{git}.}1
Summary:	A simple ball dodging game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kollision/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kollision/-/archive/%{gitbranch}/kollision-%{gitbranchd}.tar.bz2#/kollision-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kollision-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)

%description
A simple ball dodging game.

%files -f kollision.lang
%{_bindir}/kollision
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.kollision.desktop
%{_datadir}/kollision
%{_iconsdir}/*/*/apps/kollision.*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n kollision-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kollision --with-html
