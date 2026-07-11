%global tl_name bxpdfver
%global tl_revision 79071

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8b
Release:	%{tl_revision}.1
Summary:	Specify version and compression level of output PDF files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxpdfver
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpdfver.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpdfver.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package enables users to specify in their sources the following
settings on the PDF document to output: PDF version (1.4, 1.5 etc.);
whether or not to compress streams; whether or not to use object
streams. This package supports all major PDF-output engines and
dvipdfmx.

