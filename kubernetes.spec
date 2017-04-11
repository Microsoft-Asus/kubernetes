#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kubernetes
Version  : 1.6.1
Release  : 15
URL      : https://github.com/kubernetes/kubernetes/archive/v1.6.1.tar.gz
Source0  : https://github.com/kubernetes/kubernetes/archive/v1.6.1.tar.gz
Source1  : kube-apiserver.service
Source2  : kube-controller-manager.service
Source3  : kube-proxy.service
Source4  : kube-scheduler.service
Source5  : kubelet.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 CDDL-1.0 ISC LGPL-3.0 MIT MPL-2.0-no-copyleft-exception NCSA
Requires: kubernetes-bin
Requires: kubernetes-config
BuildRequires : go
BuildRequires : rsync
Patch1: 0001-kernel_validator-add-Clear-Linux-kernel-config-path.patch

%description
Gcfg reads INI-style configuration files into Go structs;
supports user-defined types and subsections.

%package bin
Summary: bin components for the kubernetes package.
Group: Binaries
Requires: kubernetes-config

%description bin
bin components for the kubernetes package.


%package config
Summary: config components for the kubernetes package.
Group: Default

%description config
config components for the kubernetes package.


%prep
%setup -q -n kubernetes-1.6.1
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491945830
make V=1 WHAT="--use_go_build cmd/kubeadm cmd/kubectl cmd/kubelet cmd/kube-proxy cmd/kube-controller-manager cmd/kube-apiserver plugin/cmd/kube-scheduler"

%install
export SOURCE_DATE_EPOCH=1491945830
rm -rf %{buildroot}
output_path="_output/bin/"
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/kube-apiserver.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/kube-controller-manager.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/kube-proxy.service
install -m 0644 %{SOURCE4} %{buildroot}/usr/lib/systemd/system/kube-scheduler.service
install -m 0644 %{SOURCE5} %{buildroot}/usr/lib/systemd/system/kubelet.service
## make_install_append content
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubeadm
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubectl
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kubelet
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-proxy
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-controller-manager
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-scheduler
install -p -m 755 -t %{buildroot}%{_bindir} ${output_path}/kube-apiserver
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kube-apiserver
/usr/bin/kube-controller-manager
/usr/bin/kube-proxy
/usr/bin/kube-scheduler
/usr/bin/kubeadm
/usr/bin/kubectl
/usr/bin/kubelet

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/kube-apiserver.service
/usr/lib/systemd/system/kube-controller-manager.service
/usr/lib/systemd/system/kube-proxy.service
/usr/lib/systemd/system/kube-scheduler.service
/usr/lib/systemd/system/kubelet.service
