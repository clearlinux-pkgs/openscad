#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openscad
Version  : 2019.01.rc1
Release  : 1
URL      : https://github.com/openscad/openscad/archive/openscad-2019.01-RC1.tar.gz
Source0  : https://github.com/openscad/openscad/archive/openscad-2019.01-RC1.tar.gz
Summary  : The programmers solid 3D CAD modeller
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 OFL-1.1
Requires: openscad-license = %{version}-%{release}
BuildRequires : CGAL-dev
BuildRequires : OpenCSG-dev
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : flex
BuildRequires : glew-dev
BuildRequires : glu-dev
BuildRequires : gmp-dev
BuildRequires : libxml2-dev
BuildRequires : mpfr-dev
BuildRequires : pkgconfig(Qt5Concurrent)
BuildRequires : pkgconfig(Qt5DBus)
BuildRequires : pkgconfig(Qt5Gamepad)
BuildRequires : pkgconfig(Qt5Multimedia)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5OpenGL)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(eigen3)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(harfbuzz)
BuildRequires : pkgconfig(libzip)
BuildRequires : qscintilla-dev

%description
Each file in this directory is a fontconfig configuration file.  Fontconfig
scans this directory, loading all files of the form [0-9][0-9]*.conf.
These files are normally installed in /usr/share/fontconfig/conf.avail
and then symlinked here, allowing them to be easily installed and then
enabled/disabled by adjusting the symlinks.

%package license
Summary: license components for the openscad package.
Group: Default

%description license
license components for the openscad package.


%prep
%setup -q -n openscad-openscad-2019.01-RC1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1546444278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openscad
cp COPYING %{buildroot}/usr/share/package-licenses/openscad/COPYING
cp examples/COPYING-CC0.txt %{buildroot}/usr/share/package-licenses/openscad/examples_COPYING-CC0.txt
cp fonts/Liberation-2.00.1/LICENSE %{buildroot}/usr/share/package-licenses/openscad/fonts_Liberation-2.00.1_LICENSE
cp testdata/ttf/liberation-2.00.1/LICENSE %{buildroot}/usr/share/package-licenses/openscad/testdata_ttf_liberation-2.00.1_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openscad/COPYING
/usr/share/package-licenses/openscad/examples_COPYING-CC0.txt
/usr/share/package-licenses/openscad/fonts_Liberation-2.00.1_LICENSE
/usr/share/package-licenses/openscad/testdata_ttf_liberation-2.00.1_LICENSE
