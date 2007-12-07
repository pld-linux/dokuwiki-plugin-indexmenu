%define		plugin		indexmenu
Summary:	Dokuwiki IndexMenu Plugin
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
This plugin allows you to insert a customizable index or a list of pages
starting from a specified namespace. It should be useful in Dokuwiki sites
where pages are organized by namespaces.

Main features are: 
- Customizable javascript themes.
- Sortable by date,title and metadata infos.
- Ajax support in order to speed it up in sites with many pages.
- Customizable context mouse menu for common page actions.
- Toc pages preview.
- Hide namespaces/pages according to your site acls settings. More info at the Acl Cache section.

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