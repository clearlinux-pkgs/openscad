#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openscad
Version  : 2019.05
Release  : 9
URL      : https://github.com/openscad/openscad/archive/openscad-2019.05/openscad-2019.05.tar.gz
Source0  : https://github.com/openscad/openscad/archive/openscad-2019.05/openscad-2019.05.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 MIT OFL-1.1 Python-2.0
Requires: openscad-bin = %{version}-%{release}
Requires: openscad-data = %{version}-%{release}
Requires: openscad-license = %{version}-%{release}
Requires: openscad-man = %{version}-%{release}
BuildRequires : CGAL-dev
BuildRequires : OpenCSG-dev
BuildRequires : bison
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : bzip2-dev
BuildRequires : double-conversion-dev
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
Patch1: 0001-Set-PREFIX-to-usr.patch
Patch2: 0002-Add-missing-header-bootlegged-by-Boost-1.72.patch
Patch3: 0003-Remove-unneeded-import-of-boost-header.patch

%description
JavaScript Libraries:
Rainbow by Craig Campbell
* https://github.com/ccampbell/rainbow
* Apache License, Version 2.0

%package bin
Summary: bin components for the openscad package.
Group: Binaries
Requires: openscad-data = %{version}-%{release}
Requires: openscad-license = %{version}-%{release}

%description bin
bin components for the openscad package.


%package data
Summary: data components for the openscad package.
Group: Data

%description data
data components for the openscad package.


%package license
Summary: license components for the openscad package.
Group: Default

%description license
license components for the openscad package.


%package man
Summary: man components for the openscad package.
Group: Default

%description man
man components for the openscad package.


%prep
%setup -q -n openscad-openscad-2019.05
cd %{_builddir}/openscad-openscad-2019.05
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake -config ltcg -config fat-static-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1592608636
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openscad
cp %{_builddir}/openscad-openscad-2019.05/COPYING %{buildroot}/usr/share/package-licenses/openscad/2436f85b95492164bda1fc52ecc05d105e959f30
cp %{_builddir}/openscad-openscad-2019.05/doc/Python-LICENSE.txt %{buildroot}/usr/share/package-licenses/openscad/de31484da051d38c60d373b7761c6c9a8e68a157
cp %{_builddir}/openscad-openscad-2019.05/examples/COPYING-CC0.txt %{buildroot}/usr/share/package-licenses/openscad/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/openscad-openscad-2019.05/fonts/Liberation-2.00.1/LICENSE %{buildroot}/usr/share/package-licenses/openscad/0898cb73de9283d38e6f4cef45ce79efbfafb0b2
cp %{_builddir}/openscad-openscad-2019.05/src/libsvg/LICENSE %{buildroot}/usr/share/package-licenses/openscad/9b61c40d214dea91f7e62b90c80ac5dfb2d207a4
cp %{_builddir}/openscad-openscad-2019.05/testdata/ttf/liberation-2.00.1/LICENSE %{buildroot}/usr/share/package-licenses/openscad/0898cb73de9283d38e6f4cef45ce79efbfafb0b2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openscad

%files data
%defattr(-,root,root,-)
/usr/share/applications/openscad.desktop
/usr/share/metainfo/org.openscad.OpenSCAD.appdata.xml
/usr/share/mime-packages/openscad.xml
/usr/share/openscad/color-schemes/editor/dark-background.json
/usr/share/openscad/color-schemes/editor/light-background.json
/usr/share/openscad/color-schemes/editor/monokai.json
/usr/share/openscad/color-schemes/editor/solarized-dark.json
/usr/share/openscad/color-schemes/editor/solarized-light.json
/usr/share/openscad/color-schemes/editor/tomorrow-night.json
/usr/share/openscad/color-schemes/editor/tomorrow.json
/usr/share/openscad/color-schemes/editor/visualstudio.json
/usr/share/openscad/color-schemes/readme.txt
/usr/share/openscad/color-schemes/render/beforedawn.json
/usr/share/openscad/color-schemes/render/deepocean.json
/usr/share/openscad/color-schemes/render/metallic.json
/usr/share/openscad/color-schemes/render/monotone.json
/usr/share/openscad/color-schemes/render/nature.json
/usr/share/openscad/color-schemes/render/solarized.json
/usr/share/openscad/color-schemes/render/starnight.json
/usr/share/openscad/color-schemes/render/sunset.json
/usr/share/openscad/color-schemes/render/tomorrow-night.json
/usr/share/openscad/color-schemes/render/tomorrow.json
/usr/share/openscad/examples/Advanced/GEB.scad
/usr/share/openscad/examples/Advanced/animation.scad
/usr/share/openscad/examples/Advanced/assert.scad
/usr/share/openscad/examples/Advanced/children.scad
/usr/share/openscad/examples/Advanced/children_indexed.scad
/usr/share/openscad/examples/Advanced/module_recursion.scad
/usr/share/openscad/examples/Advanced/offset.scad
/usr/share/openscad/examples/Advanced/surface_image.png
/usr/share/openscad/examples/Advanced/surface_image.scad
/usr/share/openscad/examples/Basics/CSG-modules.scad
/usr/share/openscad/examples/Basics/CSG.scad
/usr/share/openscad/examples/Basics/LetterBlock.scad
/usr/share/openscad/examples/Basics/linear_extrude.scad
/usr/share/openscad/examples/Basics/logo.scad
/usr/share/openscad/examples/Basics/logo_and_text.scad
/usr/share/openscad/examples/Basics/projection.scad
/usr/share/openscad/examples/Basics/projection.stl
/usr/share/openscad/examples/Basics/rotate_extrude.scad
/usr/share/openscad/examples/Basics/text_on_cube.scad
/usr/share/openscad/examples/COPYING-CC0.txt
/usr/share/openscad/examples/Functions/echo.scad
/usr/share/openscad/examples/Functions/functions.scad
/usr/share/openscad/examples/Functions/list_comprehensions.scad
/usr/share/openscad/examples/Functions/polygon_areas.scad
/usr/share/openscad/examples/Functions/recursion.scad
/usr/share/openscad/examples/Old/example001.scad
/usr/share/openscad/examples/Old/example002.scad
/usr/share/openscad/examples/Old/example003.scad
/usr/share/openscad/examples/Old/example004.scad
/usr/share/openscad/examples/Old/example005.scad
/usr/share/openscad/examples/Old/example006.scad
/usr/share/openscad/examples/Old/example007.dxf
/usr/share/openscad/examples/Old/example007.scad
/usr/share/openscad/examples/Old/example008.dxf
/usr/share/openscad/examples/Old/example008.scad
/usr/share/openscad/examples/Old/example009.dxf
/usr/share/openscad/examples/Old/example009.scad
/usr/share/openscad/examples/Old/example010.dat
/usr/share/openscad/examples/Old/example010.scad
/usr/share/openscad/examples/Old/example011.scad
/usr/share/openscad/examples/Old/example012.scad
/usr/share/openscad/examples/Old/example012.stl
/usr/share/openscad/examples/Old/example013.dxf
/usr/share/openscad/examples/Old/example013.scad
/usr/share/openscad/examples/Old/example014.scad
/usr/share/openscad/examples/Old/example015.scad
/usr/share/openscad/examples/Old/example016.scad
/usr/share/openscad/examples/Old/example016.stl
/usr/share/openscad/examples/Old/example017.scad
/usr/share/openscad/examples/Old/example018.scad
/usr/share/openscad/examples/Old/example019.scad
/usr/share/openscad/examples/Old/example020.scad
/usr/share/openscad/examples/Old/example021.scad
/usr/share/openscad/examples/Old/example022.scad
/usr/share/openscad/examples/Old/example023.scad
/usr/share/openscad/examples/Old/example024.scad
/usr/share/openscad/examples/Parametric/candleStand.json
/usr/share/openscad/examples/Parametric/candleStand.scad
/usr/share/openscad/examples/Parametric/sign.json
/usr/share/openscad/examples/Parametric/sign.scad
/usr/share/openscad/examples/examples.json
/usr/share/openscad/fonts/05-osx-fonts.conf
/usr/share/openscad/fonts/10-liberation.conf
/usr/share/openscad/fonts/Liberation-2.00.1/AUTHORS
/usr/share/openscad/fonts/Liberation-2.00.1/ChangeLog
/usr/share/openscad/fonts/Liberation-2.00.1/LICENSE
/usr/share/openscad/fonts/Liberation-2.00.1/README
/usr/share/openscad/fonts/Liberation-2.00.1/TODO
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationMono-Bold.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationMono-BoldItalic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationMono-Italic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationMono-Regular.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSans-Bold.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSans-BoldItalic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSans-Italic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSans-Regular.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSerif-Bold.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSerif-BoldItalic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSerif-Italic.ttf
/usr/share/openscad/fonts/Liberation-2.00.1/ttf/LiberationSerif-Regular.ttf
/usr/share/openscad/locale/cs/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/de/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/es/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/fr/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/pl/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/ru/LC_MESSAGES/openscad.mo
/usr/share/openscad/locale/uk/LC_MESSAGES/openscad.mo
/usr/share/pixmaps/openscad.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openscad/0898cb73de9283d38e6f4cef45ce79efbfafb0b2
/usr/share/package-licenses/openscad/2436f85b95492164bda1fc52ecc05d105e959f30
/usr/share/package-licenses/openscad/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/openscad/9b61c40d214dea91f7e62b90c80ac5dfb2d207a4
/usr/share/package-licenses/openscad/de31484da051d38c60d373b7761c6c9a8e68a157

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/openscad.1
