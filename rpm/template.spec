Name:           ros-indigo-moveit-ros-benchmarks
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS moveit_ros_benchmarks package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-moveit-ros-planning
Requires:       ros-indigo-moveit-ros-warehouse
Requires:       ros-indigo-rosconsole
Requires:       ros-indigo-roscpp
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-moveit-ros-planning
BuildRequires:  ros-indigo-moveit-ros-warehouse
BuildRequires:  ros-indigo-rosconsole
BuildRequires:  ros-indigo-roscpp

%description
MoveIt tools for benchmarking

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Dec 04 2014 Ioan Sucan <isucan@google.com> - 0.6.3-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Ioan Sucan <isucan@google.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Oct 31 2014 Ioan Sucan <isucan@google.com> - 0.6.1-0
- Autogenerated by Bloom

* Mon Oct 27 2014 Ioan Sucan <isucan@google.com> - 0.6.0-0
- Autogenerated by Bloom

