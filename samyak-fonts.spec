%global	fontname	samyak
%global fontconf	67-%{fontname}

# Common description
%global common_desc \
The Samyak package contains fonts for the display of \
Scripts Devanagari, Gujarati, Malayalam, Oriya and Tamil

Name:	 %{fontname}-fonts
Version:	1.2.2
Release:	10%{?dist}
Summary:	Free Indian truetype/opentype fonts
Group:	User Interface/X
License:	GPLv3+ with exceptions
URL:	http://sarovar.org/projects/samyak/
# Source0: http://sarovar.org/frs/?group_id=461&release_id=821
Source:	samyak-fonts-%{version}.tar.gz
Source1: 66-samyak-devanagari.conf
Source2: 67-samyak-tamil.conf
Source3: 68-samyak-malayalam.conf
Source4: 67-samyak-gujarati.conf
Source5: 67-samyak-oriya.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires: fontforge >= 20080429

%description
%common_desc

%package common
Summary:  Common files for samyak-fonts
Group:	User Interface/X
Requires: fontpackages-filesystem
%description common
%common_desc

%package -n %{fontname}-devanagari-fonts
Summary: Open Type Fonts for Devanagari script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-devanagari-fonts
This package contains truetype/opentype font for the display of \
Scripts Devanagari.

%_font_pkg -n devanagari -f 66-samyak-devanagari.conf Samyak-Devanagari.ttf 

%package -n %{fontname}-tamil-fonts
Summary: Open Type Fonts for Tamil script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-tamil-fonts
This package contains truetype/opentype font for the display of \
Scripts Tamil.

%_font_pkg -n tamil -f %{fontconf}-tamil.conf Samyak-Tamil.ttf 

%package -n %{fontname}-malayalam-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-malayalam-fonts
This package contains truetype/opentype font for the display of \
Scripts Malayalam.

%_font_pkg -n malayalam -f 68-samyak-malayalam.conf Samyak-Malayalam.ttf 

%package -n %{fontname}-gujarati-fonts
Summary: Open Type Fonts for Gujarati script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-gujarati-fonts
This package contains truetype/opentype font for the display of \
Scripts Gujarati.

%_font_pkg -n gujarati -f %{fontconf}-gujarati.conf Samyak-Gujarati.ttf 

%package -n %{fontname}-oriya-fonts
Summary: Open Type Fonts for Oriya script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-oriya-fonts
This package contains truetype/opentype font for the display of \
Scripts Oriya.

%_font_pkg -n oriya -f %{fontconf}-oriya.conf Samyak-Oriya.ttf 


%prep
%setup -q -n samyak-fonts-%{version}

%build
mkdir -p TTFfiles/
./generate.pe */*.sfd

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p TTFfiles/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/66-samyak-devanagari.conf

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tamil.conf

install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/68-samyak-malayalam.conf

install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gujarati.conf

install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-oriya.conf


for fconf in 66-samyak-devanagari.conf \
		%{fontconf}-tamil.conf \
		68-samyak-malayalam.conf \
		%{fontconf}-gujarati.conf \
		%{fontconf}-oriya.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done



%files common
%doc COPYING README AUTHORS
%dir %{_fontdir}

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> 1.2.2-9
- spec file clean up

* Tue Nov 20 2012 Pravin Satpute <psatpute@redhat.com> 1.2.2-8
- spec file clean up

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 22 2011 Pravin Satpute <psatpute@redhat.com> 1.2.2-5
- Resolved bug 714926

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Naveen Kumar <nkumar@redhat.com> - 1.2.2-3
- rectify error to directly install fonts in fontdir instead of subdir in fontdir

* Thu Jun 10 2010 Naveen Kumar <nkumar@redhat.com> 1.2.2-2
- OOPS! forgot to add pkg fontforge in BuildRequires

* Thu Jun 10 2010 Naveen Kumar <nkumar@redhat.com> 1.2.2-1
- new release from upstream with source
- changes in spec file to source compile

* Tue May 4 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-10
- remove binding="same" from all .conf files

* Thu Mar 23 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-9
- corrected ne-IN to ne-np in 67-samyak-devanagari.conf

* Wed Mar 3 2010 Naveen Kumar <nkumar@redhat.com> 1.2.1-8
- Updated .conf file
- Resolves Bug#568254

* Wed Oct 28 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-7
- added fontconf files for each subpackage

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-4
- renamed samyak-common-fonts to samyak-fonts-common

* Tue Feb 03 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-3
- renamed font package as per fedora new Font_package_naming guideline
- updated spec

* Mon Jan 12 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-2
- bugzilla 477451
- updated spec

* Thu Sep 18 2008 Pravin Satpute <psatpute@redhat.com> 1.2.1-1
- upstream release 1.2.1
- Added Unicode 5.1 support in Samyak-Devanagari 

* Fri Apr 04 2008 Pravin Satpute <psatpute@redhat.com> 1.2.0-2
- given proper license name
- fc-cache now run on samyak-langname folder

* Thu Feb 28 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.0-1
- update to samyak-fonts-1.2.0 from upstream cvs
- major bug fixes for devanagari and malayalam
- licence update to 'GNU Gplv3 or later with font exceptions'
- update spec file

* Fri Feb 08 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-2
- added sub packaging support in spec file based on lohit-fonts.spec file 

* Fri Jan 18 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-1
- initial packaging
