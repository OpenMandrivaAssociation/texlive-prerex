# revision 25004
# category Package
# catalog-ctan /graphics/prerex
# catalog-date 2012-01-02 20:49:01 +0100
# catalog-license gpl
# catalog-version 6.2
Name:		texlive-prerex
Version:	6.2
Release:	3
Summary:	Interactive editor and macro support for prerequisite charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/prerex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of prerex.sty, a LaTeX package for
producing charts of course nodes linked by arrows representing
pre- and co-requisites, and prerex, an interactive program for
creating and editing chart descriptions. The implementation of
prerex.sty is built on PGF, so that it may be used equally
happily with latex or pdflatex; prerex itself is written in C.
The package includes source code for a previewer application, a
lightweight Qt-4 and poppler-based prerex-enabled PDF viewer.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/prerex/prerex.sty
%doc %{_texmfdistdir}/doc/latex/prerex/README
%doc %{_texmfdistdir}/doc/latex/prerex/chart.html
%doc %{_texmfdistdir}/doc/latex/prerex/chart.pdf
%doc %{_texmfdistdir}/doc/latex/prerex/chart.png
%doc %{_texmfdistdir}/doc/latex/prerex/chart.tex
%doc %{_texmfdistdir}/doc/latex/prerex/doc/intro.pdf
%doc %{_texmfdistdir}/doc/latex/prerex/doc/intro.tex
%doc %{_texmfdistdir}/doc/latex/prerex/doc/introFonts.png
%doc %{_texmfdistdir}/doc/latex/prerex/doc/introchart1.tex
%doc %{_texmfdistdir}/doc/latex/prerex/doc/introchart2.tex
%doc %{_texmfdistdir}/doc/latex/prerex/doc/prerex.pdf
%doc %{_texmfdistdir}/doc/latex/prerex/doc/prerex.sty.7
%doc %{_texmfdistdir}/doc/latex/prerex/doc/prerex.tex
%doc %{_texmfdistdir}/doc/latex/prerex/prerex-6.2.tar.gz
%doc %{_texmfdistdir}/doc/latex/prerex/vprerex-6.3.1.tar.gz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
