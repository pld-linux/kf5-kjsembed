#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.116
%define		qtver		5.15.2
%define		kfname		kjsembed
#
Summary:	Binding Javascript object to QObjects
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	76a080fbbcb20654fc6ca226a1d5efc5
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kjs-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KSJEmbed provides a method of binding JavaScript objects to QObjects,
so you can script your applications.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kjscmd5
%attr(755,root,root) %{_bindir}/kjsconsole
%ghost %{_libdir}/libKF5JsEmbed.so.5
%attr(755,root,root) %{_libdir}/libKF5JsEmbed.so.*.*.*
%{_mandir}/man1/kjscmd5.1*
%lang(ca) %{_mandir}/ca/man1/kjscmd5.1*
%lang(de) %{_mandir}/de/man1/kjscmd5.1*
%lang(es) %{_mandir}/es/man1/kjscmd5.1*
%lang(it) %{_mandir}/it/man1/kjscmd5.1*
%lang(nl) %{_mandir}/nl/man1/kjscmd5.1*
%lang(pt) %{_mandir}/pt/man1/kjscmd5.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kjscmd5.1*
%lang(ru) %{_mandir}/ru/man1/kjscmd5.1*
%lang(sv) %{_mandir}/sv/man1/kjscmd5.1*
%lang(tr) %{_mandir}/tr/man1/kjscmd5.1*
%lang(uk) %{_mandir}/uk/man1/kjscmd5.1*
%lang(fr) %{_mandir}/fr/man1/kjscmd5.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KJsEmbed
%{_libdir}/cmake/KF5JsEmbed
%{_libdir}/libKF5JsEmbed.so
%{qt5dir}/mkspecs/modules/qt_KJsEmbed.pri
