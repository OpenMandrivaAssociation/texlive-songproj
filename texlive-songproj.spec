Name:		texlive-songproj
Version:	66704
Release:	1
Summary:	Generate Beamer slideshows with song lyrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/songproj
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package, together with the Beamer class, is used to
generate slideshows with song lyrics. This is typically used in
religious services in churches equipped with a projector, for
which this package has been written, but it can be useful for
any type of singing assembly. It provides environments to
describe a song in a natural way, and formatting it into slides
with overlays. The package comes with an additional Python
script that can be used to convert plain-text song lyrics to
the expected LaTeX markup.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/songproj
%{_texmfdistdir}/tex/latex/songproj
%doc %{_texmfdistdir}/doc/latex/songproj

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
