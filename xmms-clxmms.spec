Summary:	Command-Line Xmms controlling program
Summary(pl.UTF-8):	Program kontrolujący XMMS-a z linii poleceń
Name:		xmms-clxmms
Version:	0.6
Release:	4
License:	GPL
Group:		Applications/Sound
Source0:	http://kolos.math.uni.lodz.pl/~bajcik/stuff/clxmms-%{version}.tar.gz
Patch0:		clxmms.patch
# Source0-md5:	9ed0759c6e3765c0f9c2d65784db35f0
BuildRequires:	xmms-devel
BuildRequires:	readline-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Don't like GUI? This program gives you a control on a XMMS player.

%description -l pl.UTF-8
Nie lubisz interfejsu graficznego? Ten program daje Ci kontrolę nad
odtwarzaczem XMMS z linii poleceń.

%prep
%setup -q -n clxmms-%{version}
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	OPTFL="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install clxmms $RPM_BUILD_ROOT%{_bindir}
install clxmms.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
