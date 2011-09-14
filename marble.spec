#
# Conditional build:
#
%define         orgname     marble
%define         _state      stable
%define         qtver       4.7.4
#
Summary:	Marble
Summary(pl.UTF-8):	Marble
Name:		marble
Version:	4.7.1
Release:	2
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	c51019621e91c53b1ded13eb2cfc76c0
URL:		http://www.kde.org/
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
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.6.3
BuildRequires:	gpsd-devel >= 2.37
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	phonon-devel >= 4.3.1
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-kdeedu-marble < 4.6.99
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
Obsoletes:	kde4-kdeedu-devel < 4.6.99

%description devel
This package contains Marble header files.

%description devel -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe dla Marble.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geodatatest
%attr(755,root,root) %{_bindir}/marble
%attr(755,root,root) %{_bindir}/routing-instructions
%attr(755,root,root) %{_bindir}/tilecreator
%attr(755,root,root) %{_libdir}/kde4/libmarble_part.so
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_worldclock.so
%dir %{_libdir}/kde4/plugins/marble
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/AprsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CompassFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/CrosshairsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/EarthquakePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GosmorePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GpsdPositionProviderPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/GraticulePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/HostipPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LatLonPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LocalDatabasePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/LocalOsmSearchPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MapScaleFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/MonavPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NavigationFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/NominatimPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OpenDesktopPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OpenRouteServicePlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/OverviewMap.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Photo.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/PositionMarker.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/ProgressFloatItem.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/QNamNetworkPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/RoutingPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/RoutinoPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/StarsPlugin.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Weather.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/Wikipedia.so
%attr(755,root,root) %{_libdir}/kde4/plugins/marble/YoursPlugin.so
%attr(755,root,root) %ghost %{_libdir}/libmarblewidget.so.??
%attr(755,root,root) %{_libdir}/libmarblewidget.so.*.*.*
%{_datadir}/apps/marble
%{_desktopdir}/kde4/marble.desktop
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kde4/services/marble_part.desktop
%{_datadir}/kde4/services/plasma-applet-kworldclock.desktop
%{_iconsdir}/hicolor/*x*/apps/marble.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/marble
%attr(755,root,root) %{_libdir}/libmarblewidget.so
%{_datadir}/apps/cmake/modules/FindMarble.cmake
