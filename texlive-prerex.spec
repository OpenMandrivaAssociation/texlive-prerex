%global tl_name prerex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Interactive editor and macro support for prerequisite charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/prerex
License:	gpl2 lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package consists of prerex.sty, a LaTeX package for producing
charts of course nodes linked by arrows representing pre- and co-
requisites, and prerex, an interactive program for creating and editing
chart descriptions. The implementation of prerex.sty uses PGF, so that
it may be used equally happily with LaTeX or pdfLaTeX; prerex itself is
written in C. The package includes source code for a previewer
application, a lightweight Qt-4 and poppler-based prerex-enabled PDF
viewer.

