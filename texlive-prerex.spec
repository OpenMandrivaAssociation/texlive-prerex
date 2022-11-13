Name:		texlive-prerex
Version:	54512
Release:	1
Summary:	Interactive editor and macro support for prerequisite charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/prerex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/prerex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of prerex.sty, a LaTeX package for
producing charts of course nodes linked by arrows representing
pre- and co-requisites, and prerex, an interactive program for
creating and editing chart descriptions. The implementation of
prerex.sty uses PGF, so that it may be used equally happily
with latex or pdflatex; prerex itself is written in C. The
package includes source code for a previewer application, a
lightweight Qt-4 and poppler-based prerex-enabled PDF viewer.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/prerex
%doc %{_texmfdistdir}/doc/latex/prerex
%doc %{_mandir}/man5/prerex.5*
%doc %{_texmfdistdir}/doc/man/man5/prerex.man5.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdistdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
