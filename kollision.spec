Name:		kollision
Version:	15.08.2
Release:	1
Epoch:		1
Summary:	A simple ball dodging game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/kollision/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)

%description -n kollision
A simple ball dodging game.

%files
%{_bindir}/kollision
%{_datadir}/appdata/*.xml
%{_datadir}/applications/org.kde.kollision.desktop
%{_datadir}/kollision
%{_datadir}/kxmlgui5/kollision
%{_iconsdir}/*/*/apps/kollision.*
%doc %{_docdir}/*/*/kollision

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
