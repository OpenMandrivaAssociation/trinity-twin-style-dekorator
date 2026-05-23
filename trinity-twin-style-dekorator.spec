%bcond clang 1

# TDE variables
%define tde_pkg twin-style-dekorator
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Semi transparant window decoration for Trinity
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/themes/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DSYSCONF_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Crystal offers you pseudo transparent titlebar, buttons and borders
transparent, so you can see more of your lovely background image
Transparancy and buttons can be costumized to match your wishes.
Offers rounded corners as well

And it is of course nice to look at. Upstream says:
"- Don't forget to breathe, while drooling."


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{tde_prefix}/%{_lib}/trinity/twin3_deKorator.la
%{tde_prefix}/%{_lib}/trinity/twin3_deKorator.so
%{tde_prefix}/%{_lib}/trinity/twin_deKorator_config.la
%{tde_prefix}/%{_lib}/trinity/twin_deKorator_config.so
%{tde_prefix}/share/apps/deKorator/
%{tde_prefix}/share/apps/twin/deKorator.desktop

