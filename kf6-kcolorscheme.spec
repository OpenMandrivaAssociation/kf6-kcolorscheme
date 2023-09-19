%define libname %mklibname KF6ColorScheme
%define devname %mklibname KF6ColorScheme -d
%define git 20230918

Name: kf6-kcolorscheme
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kcolorscheme/-/archive/master/kcolorscheme-master.tar.bz2#/kcolorscheme-%{git}.tar.bz2
Summary: Classes to read and interact with KColorScheme
URL: https://invent.kde.org/frameworks/kcolorscheme
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
# Just to make sure we don't pull the KDE5 Version
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Classes to read and interact with KColorScheme

%package -n %{libname}
Summary: Classes to read and interact with KColorScheme
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Classes to read and interact with KColorScheme

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Classes to read and interact with KColorScheme

%prep
%autosetup -p1 -n kcolorscheme-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kcolorscheme.*

%files -n %{devname}
%{_includedir}/KF6/KColorScheme
%{_libdir}/cmake/KF6ColorScheme
%{_qtdir}/mkspecs/modules/qt_KColorScheme.pri
%{_qtdir}/doc/KF6ColorScheme.*

%files -n %{libname}
%{_libdir}/libKF6ColorScheme.so*
