#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_serviceengine
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServiceEngine Avi RESTful Object
description:
    - This module is used to configure ServiceEngine object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    availability_zone:
        description:
            - Availability_zone of serviceengine.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
        type: str
    container_mode:
        description:
            - Boolean flag to set container_mode.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    container_type:
        description:
            - Enum options - CONTAINER_TYPE_BRIDGE, CONTAINER_TYPE_HOST, CONTAINER_TYPE_HOST_DPDK.
            - Default value when not specified in API or module is interpreted by Avi Controller as CONTAINER_TYPE_HOST.
        type: str
    controller_created:
        description:
            - Boolean flag to set controller_created.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    controller_ip:
        description:
            - Controller_ip of serviceengine.
        type: str
    data_vnics:
        description:
            - List of vnic.
        type: list
    enable_state:
        description:
            - Inorder to disable se set this field appropriately.
            - Enum options - SE_STATE_ENABLED, SE_STATE_DISABLED_FOR_PLACEMENT, SE_STATE_DISABLED, SE_STATE_DISABLED_FORCE.
            - Default value when not specified in API or module is interpreted by Avi Controller as SE_STATE_ENABLED.
        type: str
    flavor:
        description:
            - Flavor of serviceengine.
        type: str
    host_ref:
        description:
            - It is a reference to an object of type vimgrhostruntime.
        type: str
    hypervisor:
        description:
            - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
        type: str
    mgmt_vnic:
        description:
            - Vnic settings for serviceengine.
        type: dict
    name:
        description:
            - Name of the object.
            - Default value when not specified in API or module is interpreted by Avi Controller as VM name unknown.
        type: str
    resources:
        description:
            - Seresources settings for serviceengine.
        type: dict
    se_group_ref:
        description:
            - It is a reference to an object of type serviceenginegroup.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Unique object identifier of the object.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create ServiceEngine object
  vmware.alb.avi_serviceengine:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_serviceengine
"""

RETURN = '''
obj:
    description: ServiceEngine (api/serviceengine) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        availability_zone=dict(type='str',),
        cloud_ref=dict(type='str',),
        container_mode=dict(type='bool',),
        container_type=dict(type='str',),
        controller_created=dict(type='bool',),
        controller_ip=dict(type='str',),
        data_vnics=dict(type='list',),
        enable_state=dict(type='str',),
        flavor=dict(type='str',),
        host_ref=dict(type='str',),
        hypervisor=dict(type='str',),
        mgmt_vnic=dict(type='dict',),
        name=dict(type='str',),
        resources=dict(type='dict',),
        se_group_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'serviceengine',
                           set())


if __name__ == '__main__':
    main()
