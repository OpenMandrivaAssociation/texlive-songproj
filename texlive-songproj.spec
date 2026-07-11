%global tl_name songproj
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.0
Release:	%{tl_revision}.1
Summary:	Generate Beamer slideshows with song lyrics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/songproj
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/songproj.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package, together with the Beamer class, is used to generate
slideshows with song lyrics. This is typically used in religious
services in churches equipped with a projector, for which this package
has been written, but it can be useful for any type of singing assembly.
It provides environments to describe a song in a natural way, and
formatting it into slides with overlays. The package comes with an
additional Python script that can be used to convert plain-text song
lyrics to the expected LaTeX markup.

