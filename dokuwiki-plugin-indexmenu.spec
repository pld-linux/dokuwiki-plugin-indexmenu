%define		plugin		indexmenu
Summary:	DokuWiki IndexMenu plugin
Summary(pl.UTF-8):	Wtyczka IndexMenu dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20071026
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://samuele.netsons.org/dokuwiki/media/indexmenu.zip
# Source0-md5:	6b0f031c00a636d7ccfa26f5111e6d8f
URL:		http://wiki.splitbrain.org/plugin:indexmenu
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{plugin}

%description
This plugin allows you to insert a customizable index or a list of
pages starting from a specified namespace. It should be useful in
DokuWiki sites where pages are organized by namespaces.

Main features are: 
- Customizable JavaScript themes.
- Sortable by date, title and metadata infos.
- Ajax support in order to speed it up in sites with many pages.
- Customizable context mouse menu for common page actions.
- Toc pages preview.
- Hide namespaces/pages according to your site ACLs settings

%description -l pl.UTF-8
Ta wtyczka pozwala na umieszczenie konfigurowalnego indeksu lub listy
stron rozpoczynającej się od określonej przestrzeni nazw. Powinna być
przydatna w serwisach DokuWiki, w których strony są zorganizowane w
przestrzenie nazw.

Główne możliwości obejmują:
- konfigurowalne motywy w JavaScripcie,
- sortowanie po dacie, tytule i metadanych,
- obsługa Ajaksa w celu przyspieszenia serwisów z wieloma stronami,
- konfigurowalne menu kontekstowe myszy z często wykonywanymi
  czynnościami dla strony,
- podgląd stron spisu treści,
- ukrywanie przestrzeni nazw i stron zgodnie z ustawieniami ACL
  serwisu.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}
rm -f $RPM_BUILD_ROOT%{_plugindir}/{CREDITS,changelog}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS changelog
%{_plugindir}
