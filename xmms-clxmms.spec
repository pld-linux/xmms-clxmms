Summary:	Command-Line Xmms controlling program
Summary(pl):	Program kontroluj�cy xmms z linii polece�
Name:		xmms-clxmms
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(pl):	Aplikacje/D�wi�k
Group(pt_BR):	Aplica��es/Som
Source0:	http://kolos.math.uni.lodz.pl/~bajcik/stuff/clxmms-%{version}.tar.gz
BuildRequires:	xmms-devel
BuildRequires:	readline-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Don't like GUI? This program gives you a control on a xmms player.

%description -l pl
Nie lubisz interfejsu graficznego? Ten program daje Ci kontrol� nad
odtwarzaczem xmms.

%prep
%setup -q -n clxmms-%{version}

%build
%{__make} \
	CC=%{__cc} \
	OPTFL="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install clxmms $RPM_BUILD_ROOT%{_bindir}
install clxmms.1 $RPM_BUILD_ROOT%{_mandir}/man1/

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
