
Infrastructure Code is still in progress.. goal is to build a production lab end-to-end deployment with various topologies products in a single click of button, the same can be used in specfic prod automations. 

## Description

This repository contains Ansible scripts that perform fully automated deployments of complete nested VMware SDDC  contains:
* vCenter Server
* ESXi Hosts
* NSX-T Local Manager
* NSX-T Edge Nodes


The primary use case is consistent and speedy provisioning of nested VMware SDDC lab environments.

## Requirements
The following are the requirements for successful Pod deployments:

* A physical ESXi host running version 6.7 or higher.
* A virtual machine with a modern version of Ubuntu (used as the Ansible controller)
* The default deployment settings require DNS name resolution. You can leverage an existing DNS server, but it must be configured with the required forward and reverse zones and support dynamic updates.
* Access to VMware product installation media.
* For deploying NSX-T you will need an NSX-T license (Check out [VMUG Advantage](https://www.vmug.com/membership/vmug-advantage-membership) or the [NSX-T Product Evaluation Center](https://my.vmware.com/web/vmware/evalcenter?p=nsx-t-eval)).


### Recommendations
The following are recommendations based on our experience with deploying SDDC:

* Use a physical layer-3 switch with appropriate OSPF/BGP configuration matching the OSPF/BGP settings in your config.yml file. Dynamic routing between your SDDC and your physical network will make for a better experience.
* Hardware configuration of the physical ESXi host(s):
  * 2 CPUs (10 cores per CPU)
  * 320 GB RAM
  * 1 TB storage capacity (preferably SSD). Either DAS or 10 Gbit NFS/iSCSI.  More space required if multiple labs are deployed.
* Virtual hardware configuration of the Ansible controller VM:
  * 1 vCPU (4 vCPUs recommended)
  * 8 GB RAM (16GB RAM recommended)
  * Hard disk
    * 64 GB for Linux boot disk
    * 300 GB for /Software repository (Recommend this be on it's own disk)
  * VMware Paravirtual SCSI controller
  * VMXNET 3 network adapter
* Deploy the pre-configured DNS server for DNS name resolution within SDDC instead of using your own.
 
## Preparations

* Configure your physical network:
  * Create an Lab-Routers VLAN used as transit segment between your layer-3 switch and the SDDC NSXT
  * Configure routing (OSPFv2/OSPFv3/BGP/static) on the Lab-Routers segment.
  * Add the SDDC VLANs to your layer-3 switch in case you are deploying the Pod to a vSphere cluster. 

* Install the required software on your Ansible controller:
  * sudo apt install python3 python3-pip xorriso git
  * sudo pip3 install ansible pyvim pyvmomi netaddr jmespath dnspython
  * ansible-galaxy collection install community.general community.vmware ansible.posix
  * git clone https://github.com/virtualsachin/SDDC.git

* Copy/rename the sample files:
  * cp licenses_sample.yml licenses.yml
 

* Modify  **licenses.yml** according to your needs and your environment

* Create the Software Library directory structure using:
  * sudo ansible-playbook utils/util_CreateSoftwareDir.yml

* Add installation media to the corresponding directories in the Software Library (/Software)


## Networking
The network configuration is where many users experience issues with the setup of the SDDC.Lab solution.  For that reason, the focus of this section is to give a deep dive into how the SDDC.Lab solution "connects" to the physical network, and what networking components it requires.  We will also give overviews of how the network connectivity is different if you're running:
* 1 Physical Server
* 2 Physical Servers
* 3 (or more) Physical Servers


### Physical Networking Overview
When we refer to physical networking, we are referring to the "NetLab-L3-Switch" in the network diagram shown above, along with the "Lab-Routers" portgroup to which it connects.  The "Lab-Routers" portgroup is the central "meet-me" network segment which all SDDC connect to.  It's here where the various SDDC establish OSPFv2, OSPFv3, and BGP neighbor peerings and share routes.  Because OSPF uses multicast to discovery neighbors, there is no additional configuration required for it.  BGP on the other hand, by default, is only configured to peer with the "NetLab-L3-Switch".  This behavior can be changed by adding additional neighbors to the Pod Configuration file, but that is left up to the user to setup.

To ensure VLAN IDs created on the "NetLab-L3-Switch" do not pollute other networking environments, and to protect the production network from the SDDC.Lab environment, it's **HIGHLY** recommended that the following guidelines are followed:
1. The VLAN IDs used by the SDDC.Lab environment (i.e. VLANs 10-249) should not be stretched to other switches outside of the SDDC.Lab environment.  Those VLANs should be local to the SDDC.Lab.
2. The uplink from the "NetLab-L3-Switch" to the core network should be a **ROUTED** connection.
3. Reachability between the SDDC.Lab environment and the Core Network should be via static routes, and **NOT** use any dynamic routing protocol.  This will ensure that SDDC.Lab routes don't accidentally "leak" into the production network.

All interfaces, both virtual and physical, that are connected to the "Lab-Routers" segment should be configured with a 1500 byte MTU.  This ensures that OSPF neighbors can properly establish peering relationships.  That said, the "NetLab-L3-Switch" must be configured to support jumbo mtu frames, as multiple SDDC.Lab segments require jumbo frame support.  Jumbo frame size of 9000 (or higher) is suggested.

### Physical Network Considerations - One ESXi Server
When only one physical ESXi server is being used to run Pod workloads, as all workloads will be running on the same vSwitch on that host, there is no requirement to configure an Uplink on the SDDCLab_vDS switch to the physical environment.

### Physical Network Considerations - Two ESXi Servers
When exactly two physical ESXi servers are being used to run Pod workloads, you can use a cross-over cable to connect the SDDCLab_vDS vswitches together via their Uplinks.  This cable between the two servers to connect the SDDCLab_vDS Uplink interface from each server.

### Physical Network Considerations - Three or more ESXi Servers
When three or more physical ESXi servers are being used to run Pod workloads, you have two options:
1. Use a single "NetLab-L3-Switch" and connect all servers to it (Suggested)
2. If the number of available ports on the "NetLab-L3-Switch" is limited, you can use two switches as is shown in the Pod Logical Networking Overview above.  In this configuration, a layer-2 only switch is used for the SDDCLab_vDS vswitch, and a layer-3 switch is used to connect to the "Lab-Routers" segment.

