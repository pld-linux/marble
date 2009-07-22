#
# Conditional build:
#
%define		qt_ver		4.5.2
%define		_kdever		4.2.4

Summary:	Marble
Summary(pl.UTF-8):	Marble
Name:		marble
Version:	0.7.1
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	http://developer.kde.org/~tackat/marble_0_7/%{name}-%{version}_rev938110.tar.gz
# Source0-md5:	6073ecc2b944e944e42e6b6218cf6473
URL:		http://edu.kde.org/marble/
# leave only required ones
BuildRequires:	Qt3Support-devel >= %{qt_ver}
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	QtDesigner-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtScript-devel >= %{qt_ver}
BuildRequires:	QtSvg-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	QtUiTools-devel >= %{qt_ver}
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marble is a Virtual Globe and World Atlas that you can use to learn
more about Earth: You can pan and zoom around and you can look up
places and roads. A mouse click on a place label will provide the
respective Wikipedia article.

%description -l pl.UTF-8
Marble.

%package devel
Summary:	Marble header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla Marble
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kde4-kdelibs-devel >= %{version}

%description devel
This package contains Marble header files.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe dla Marble.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geodatatest
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/tilecreator
%attr(755,root,root) %{_libdir}/kde4/libmarble_part.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_worldclock.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CompassFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MapScaleFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MarbleCrosshairsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MarbleGeoDataPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MarbleOverviewMap.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MarbleStarsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NavigationFloatItem.so
%attr(755,root,root) %ghost %{_libdir}/libmarblewidget.so.?
%attr(755,root,root) %{_libdir}/libmarblewidget.so.*.*.*
%{_datadir}/apps/marble
%{_desktopdir}/kde4/marble.desktop
%{_datadir}/apps/marble_part/marble_part.rc
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kde4/services/marble_part.desktop
%{_datadir}/kde4/services/plasma-applet-kworldclock.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/marble
%attr(755,root,root) %{_libdir}/libmarblewidget.so
%{_datadir}/apps/cmake/modules/FindMarble.cmake
