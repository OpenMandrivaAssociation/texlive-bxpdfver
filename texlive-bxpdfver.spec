Name:		texlive-bxpdfver
Version:	63185
Release:	2
Summary:	Specify version and compression level of output PDF files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxpdfver
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpdfver.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpdfver.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package enables users to specify in their sources the
following settings on the PDF document to output: PDF version
(1.4, 1.5 etc.); whether or not to compress streams; whether or
not to use object streams. This package supports all major
PDF-output engines and dvipdfmx.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxpdfver
%doc %{_texmfdistdir}/doc/latex/bxpdfver

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
