.. vmware.alb.avi_virtualservice:


**********************************************
vmware.alb.avi_virtualservice
**********************************************

**Module for setup of VirtualService Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure VirtualService object.
- More examples at (https://github.com/avinetworks/devops).


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li>absent</li>
                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - The state that should be applied on the entity.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_update_method</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>put</b>&nbsp;&larr;</div></li>
                    <li>patch</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Default method for object update is HTTP PUT.
                </div>
                <div style="font-size: small">
                    - Setting to patch will override that behavior to use HTTP PATCH.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_patch_op</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>add</b>&nbsp;&larr;</div></li>
                    <li>replace</li>
                    <li>delete</li>
                    <li>remove</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Patch operation to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_path</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch path to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_value</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch value to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>active_standby_se_tag</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - This configuration only applies if the virtualservice is in legacy active standby ha mode and load distribution among active standby is enabled.
                </div>
                                <div style="font-size: small">
                  - This field is used to tag the virtualservice so that virtualservices with the same tag will share the same active serviceengine.
                </div>
                                <div style="font-size: small">
                  - Virtualservices with different tags will have different active serviceengines.
                </div>
                                <div style="font-size: small">
                  - If one of the serviceengine's in the serviceenginegroup fails, all virtualservices will end up using the same active serviceengine.
                </div>
                                <div style="font-size: small">
                  - Redistribution of the virtualservices can be either manual or automated when the failed serviceengine recovers.
                </div>
                                <div style="font-size: small">
                  - Redistribution is based on the auto redistribute property of the serviceenginegroup.
                </div>
                                <div style="font-size: small">
                  - Enum options - ACTIVE_STANDBY_SE_1, ACTIVE_STANDBY_SE_2.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as ACTIVE_STANDBY_SE_1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>advertise_down_vs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Keep advertising virtual service via bgp even if it is marked down by health monitor.
                </div>
                                <div style="font-size: small">
                  - This setting takes effect for future virtual service flaps.
                </div>
                                <div style="font-size: small">
                  - To advertise current vses that are down, please disable and re-enable the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>allow_invalid_client_cert</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Process request even if invalid client certificate is presented.
                </div>
                                <div style="font-size: small">
                  - Datascript apis need to be used for processing of such requests.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>analytics_policy</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Determines analytics settings for the application.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>analytics_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specifies settings related to analytics.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type analyticsprofile.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>apic_contract_graph</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The name of the contract/graph associated with the virtual service.
                </div>
                                <div style="font-size: small">
                  - Should be in the <contract name> <graph name> format.
                </div>
                                <div style="font-size: small">
                  - This is applicable only for service integration mode with cisco apic controller.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.12,18.1.2.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>application_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable application layer specific features for the virtual service.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type applicationprofile.
                </div>
                                <div style="font-size: small">
                  - Special default for essentials edition is system-l4-application.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_allocate_floating_ip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Auto-allocate floating/elastic ip from the cloud infrastructure.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>auto_allocate_ip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Auto-allocate vip from the provided subnet.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>availability_zone</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Availability-zone to place the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_allocated_fip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) fip allocated by avi in the cloud infrastructure.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_allocated_vip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) vip allocated by avi in the cloud infrastructure.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>azure_availability_set</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use)applicable for azure only.
                </div>
                                <div style="font-size: small">
                  - Azure availability set to which this vs is associated.
                </div>
                                <div style="font-size: small">
                  - Internally set by the cloud connector.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.12, 18.1.2.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>bgp_peer_labels</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select bgp peers, using peer label, for vsvip advertisement.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Maximum of 128 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>bot_policy_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Bot detection policy for the virtual service.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type botdetectionpolicy.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>bulk_sync_kvcache</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (this is a beta feature).
                </div>
                                <div style="font-size: small">
                  - Sync key-value cache to the new ses when vs is scaled out.
                </div>
                                <div style="font-size: small">
                  - For ex  ssl sessions are stored using vs's key-value cache.
                </div>
                                <div style="font-size: small">
                  - When the vs is scaled out, the ssl session information is synced to the new se, allowing existing ssl sessions to be reused on the new se.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.7, 18.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>client_auth</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Http authentication configuration for protected resources.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 21.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>close_client_conn_on_config_update</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Close client connection on vs config update.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.4.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cloud_config_cksum</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Checksum of cloud configuration for vs.
                </div>
                                <div style="font-size: small">
                  - Internally set by cloud connector.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cloud_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type cloud.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>cloud_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
                </div>
                                <div style="font-size: small">
                  - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- cloud_none,cloud_nsxt) edition, essentials(allowed values- cloud_none,cloud_vcenter) edition, enterprise
                </div>
                                <div style="font-size: small">
                  - edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>configpb_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Protobuf versioning for config pbs.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>connections_rate_limit</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Rate limit the incoming connections to this virtual service.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>content_rewrite</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Profile used to match and rewrite strings in request and/or response body.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>created_by</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Creator name.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>delay_fairness</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select the algorithm for qos fairness.
                </div>
                                <div style="font-size: small">
                  - This determines how multiple virtual services sharing the same service engines will prioritize traffic over a congested network.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>description</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - User defined description for the object.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>discovered_network_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) discovered networks providing reachability for client facing virtual service ip.
                </div>
                                <div style="font-size: small">
                  - This field is deprecated.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type network.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>discovered_networks</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) discovered networks providing reachability for client facing virtual service ip.
                </div>
                                <div style="font-size: small">
                  - This field is used internally by avi, not editable by the user.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>discovered_subnet</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) discovered subnets providing reachability for client facing virtual service ip.
                </div>
                                <div style="font-size: small">
                  - This field is deprecated.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dns_info</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.
                </div>
                                <div style="font-size: small">
                  - Note that only one of fqdn and dns_info setting is allowed.
                </div>
                                <div style="font-size: small">
                  - Maximum of 1000 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>dns_policies</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Dns policies applied on the dns traffic of the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>east_west_placement</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Force placement on all se's in service group (mesos mode only).
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_autogw</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Response traffic to clients will be sent back to the source mac address of the connection, rather than statically sent to a default gateway.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Special default for basic edition is false, essentials edition is false, enterprise is true.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_rhi</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable route health injection using the bgp config in the vrf context.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enable_rhi_snat</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable route health injection for source nat'ted floating ip address using the bgp config in the vrf context.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>enabled</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Enable or disable the virtual service.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>error_page_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Error page profile to be used for this virtualservice.this profile is used to send the custom error page to the client generated by the proxy.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type errorpageprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.4.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>floating_ip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Floating ip to associate with this virtual service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>floating_subnet_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - If auto_allocate_floating_ip is true and more than one floating-ip subnets exist, then the subnet for the floating ip address allocation.
                </div>
                                <div style="font-size: small">
                  - This field is applicable only if the virtualservice belongs to an openstack or aws cloud.
                </div>
                                <div style="font-size: small">
                  - In openstack or aws cloud it is required when auto_allocate_floating_ip is selected.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>flow_dist</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Criteria for flow distribution among ses.
                </div>
                                <div style="font-size: small">
                  - Enum options - LOAD_AWARE, CONSISTENT_HASH_SOURCE_IP_ADDRESS, CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- load_aware) edition, essentials(allowed values- load_aware) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as LOAD_AWARE.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>flow_label_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Criteria for flow labelling.
                </div>
                                <div style="font-size: small">
                  - Enum options - NO_LABEL, APPLICATION_LABEL, SERVICE_LABEL.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as NO_LABEL.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>fqdn</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Dns resolvable, fully qualified domain name of the virtualservice.
                </div>
                                <div style="font-size: small">
                  - Only one of 'fqdn' and 'dns_info' configuration is allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>host_name_xlate</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Translate the host name sent to the servers to this value.
                </div>
                                <div style="font-size: small">
                  - Translate the host name sent from servers back to the value used by the client.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>http_policies</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Http policies applied on the data traffic of the virtual service.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>icap_request_profile_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The config settings for the icap server when checking the http request.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type icapprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Maximum of 1 items allowed.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ign_pool_net_reach</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ignore pool servers network reachability constraints for virtual service placement.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ip_address</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Ip address of the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ipam_network_subnet</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Subnet and/or network for allocating virtualservice ip by ipam provider module.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>jwt_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Application-specific config for jwt validation.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>l4_policies</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - L4 policies applied to the data traffic of the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.7.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>labels</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Key value pairs for granular object access control.
                </div>
                                <div style="font-size: small">
                  - Also allows for classification and tagging of similar objects.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.2.
                </div>
                                <div style="font-size: small">
                  - Maximum of 4 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ldap_vs_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Application-specific ldap config.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>limit_doser</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Limit potential dos attackers who exceed max_cps_per_client significantly to a fraction of max_cps_per_client for a while.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>markers</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of labels to be used for granular rbac.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.5.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>max_cps_per_client</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Maximum connections per second per client ip.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 10-1000.
                </div>
                                <div style="font-size: small">
                  - Special values are 0- 'unlimited'.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 0.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>microservice_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Microservice representing the virtual service.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type microservice.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>min_pools_up</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Minimum number of up pools to mark vs up.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.1, 17.2.12.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Name for the virtual service.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>network_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Determines network settings such as protocol, tcp or udp, and related options for the protocol.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type networkprofile.
                </div>
                                <div style="font-size: small">
                  - Special default for essentials edition is system-tcp-fast-path.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>network_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Manually override the network on which the virtual service is placed.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type network.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>network_security_policy_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Network security policies for the virtual service.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type networksecuritypolicy.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>nsx_securitygroup</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - A list of nsx groups representing the clients which can access the virtual ip of the virtual service.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>oauth_vs_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Virtualservice specific oauth config.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>performance_limits</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Optional settings that determine performance limits like max connections or bandwdith etc.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pool_group_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The pool group is an object that contains pools.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type poolgroup.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>pool_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The pool is an object that contains destination servers and related attributes such as load-balancing and persistence.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pool.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>port_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - (internal-use) network port assigned to the virtual service ip address.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>remove_listening_port_on_vs_down</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Remove listening port if virtualservice is down.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>requests_rate_limit</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Rate limit the incoming requests to this virtual service.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>saml_sp_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Application-specific saml config.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>scaleout_ecmp</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Disable re-distribution of flows across service engines for a virtual service.
                </div>
                                <div style="font-size: small">
                  - Enable if the network itself performs flow hashing with ecmp in environments such as gcp.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>se_group_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The service engine group to use for this virtual service.
                </div>
                                <div style="font-size: small">
                  - Moving to a new se group is disruptive to existing connections for this vs.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type serviceenginegroup.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>security_policy_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Security policy applied on the traffic of the virtual service.
                </div>
                                <div style="font-size: small">
                  - This policy is used to perform security actions such as distributed denial of service (ddos) attack mitigation, etc.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type securitypolicy.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>server_network_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Determines the network settings profile for the server side of tcp proxied connections.
                </div>
                                <div style="font-size: small">
                  - Leave blank to use the same settings as the client to vs side of the connection.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type networkprofile.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_metadata</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Metadata pertaining to the service provided by this virtual service.
                </div>
                                <div style="font-size: small">
                  - In openshift/kubernetes environments, egress pod info is stored.
                </div>
                                <div style="font-size: small">
                  - Any user input to this field will be overwritten by avi vantage.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>service_pool_select</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select pool based on destination port.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>services</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of services defined for this virtual service.
                </div>
                                <div style="font-size: small">
                  - Maximum of 2048 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sideband_profile</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Sideband configuration to be used for this virtualservice.it can be used for sending traffic to sideband vips for external inspection etc.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>snat_ip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Nat'ted floating source ip address(es) for upstream connection to servers.
                </div>
                                <div style="font-size: small">
                  - Maximum of 32 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sp_pool_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Gslb pools used to manage site-persistence functionality.
                </div>
                                <div style="font-size: small">
                  - Each site-persistence pool contains the virtualservices in all the other sites, that is auto-generated by the gslb manager.
                </div>
                                <div style="font-size: small">
                  - This is a read-only field for the user.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type pool.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.2.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_key_and_certificate_refs</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select or create one or two certificates, ec and/or rsa, that will be presented to ssl/tls terminated connections.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslkeyandcertificate.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Determines the set of ssl versions and ciphers to accept for ssl/tls terminated connections.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type sslprofile.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_profile_selectors</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Select ssl profile based on client ip address match.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ssl_sess_cache_avg_size</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Expected number of ssl session cache entries (may be exceeded).
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1024-16383.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sso_policy</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Client authentication and authorization policy for the virtualservice.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>sso_policy_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The sso policy attached to the virtualservice.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type ssopolicy.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>static_dns_records</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of static dns records applied to this virtual service.
                </div>
                                <div style="font-size: small">
                  - These are static entries and no health monitoring is performed against the ip addresses.
                </div>
                                <div style="font-size: small">
                  - Maximum of 1000 items allowed.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>subnet</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Subnet providing reachability for client facing virtual service ip.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>subnet_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - It represents subnet for the virtual service ip address allocation when auto_allocate_ip is true.it is only applicable in openstack or aws cloud.
                </div>
                                <div style="font-size: small">
                  - This field is required if auto_allocate_ip is true.
                </div>
                                <div style="font-size: small">
                  - Field deprecated in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>test_se_datastore_level_1_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Used for testing se datastore upgrade 2.0 functionality.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type testsedatastorelevel1.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>topology_policies</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Topology policies applied on the dns traffic of the virtual service based ongslb topology algorithm.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>traffic_clone_profile_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Server network or list of servers for cloning traffic.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type trafficcloneprofile.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>traffic_enabled</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Knob to enable the virtual service traffic on its assigned service engines.
                </div>
                                <div style="font-size: small">
                  - This setting is effective only when the enabled flag is set to true.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.8.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specify if this is a normal virtual service, or if it is the parent or child of an sni-enabled virtual hosted virtual service.
                </div>
                                <div style="font-size: small">
                  - Enum options - VS_TYPE_NORMAL, VS_TYPE_VH_PARENT, VS_TYPE_VH_CHILD.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- vs_type_normal,vs_type_vh_parent) edition, essentials(allowed values- vs_type_normal) edition, enterprise
                </div>
                                <div style="font-size: small">
                  - edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as VS_TYPE_NORMAL.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Avi controller URL of the object.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_bridge_ip_as_vip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Use bridge ip as vip on each host in mesos deployments.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- false) edition, essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_vip_as_snat</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Use the virtual ip as the snat ip for health monitoring and sending traffic to the backend servers instead of the service engine interface ip.
                </div>
                                <div style="font-size: small">
                  - The caveat of enabling this option is that the virtualservice cannot be configued in an active-active ha mode.
                </div>
                                <div style="font-size: small">
                  - Dns based multi vip solution has to be used for ha & non-disruptive upgrade purposes.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.9,17.2.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials(allowed values- false) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Uuid of the virtualservice.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vh_domain_name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The exact name requested from the client's sni-enabled tls hello domain name field.
                </div>
                                <div style="font-size: small">
                  - If this is a match, the parent vs will forward the connection to this child vs.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vh_matches</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Host and path match criteria to select this child vs.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vh_parent_vs_uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specifies the virtual service acting as virtual hosting (sni) parent.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vh_type</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Specify if the virtual hosting vs is of type sni or enhanced.
                </div>
                                <div style="font-size: small">
                  - Enum options - VS_TYPE_VH_SNI, VS_TYPE_VH_ENHANCED.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- vs_type_vh_enhanced) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Special default for basic edition is vs_type_vh_enhanced, enterprise is vs_type_vh_sni.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as VS_TYPE_VH_SNI.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vip</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - List of virtual service ips.
                </div>
                                <div style="font-size: small">
                  - While creating a 'shared vs',please use vsvip_ref to point to the shared entities.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vrf_context_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Virtual routing context that the virtual service is bound to.
                </div>
                                <div style="font-size: small">
                  - This is used to provide the isolation of the set of networks the application is attached to.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type vrfcontext.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vs_datascripts</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">list</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Datascripts applied on the data traffic of the virtual service.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vsvip_cloud_config_cksum</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Checksum of cloud configuration for vsvip.
                </div>
                                <div style="font-size: small">
                  - Internally set by cloud connector.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.9, 18.1.2.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>vsvip_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Mostly used during the creation of shared vs, this field refers to entities that can be shared across virtual services.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type vsvip.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_policy_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Waf policy for the virtual service.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type wafpolicy.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 17.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic edition, essentials edition, enterprise edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>weight</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - The quality of service weight to assign to traffic transmitted from this virtual service.
                </div>
                                <div style="font-size: small">
                  - A higher weight will prioritize traffic versus other virtual services sharing the same service engines.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 1-128.
                </div>
                                <div style="font-size: small">
                  - Allowed in basic(allowed values- 1) edition, essentials(allowed values- 1) edition, enterprise edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 1.
                </div>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - hosts: localhost
      connection: local
      collections:
        - vmware.alb
      vars:
        avi_credentials:
          username: "{{ username }}"
          password: "{{ password }}"
          controller: "{{ controller }}"
          api_version: "{{ api_version }}"
      tasks:        
        - name: Create SSL Virtual Service using Pool testpool2
          avi_virtualservice:
            avi_credentials: "{{ avi_credentials }}"
            name: newtestvs
            state: present
            performance_limits:
            max_concurrent_connections: 1000
            vsvip_ref: /api/vsvip/?name=vsvip-newtestvs-Default-Cloud
            services:
                - port: 443
                  enable_ssl: true
                - port: 80
            ssl_profile_ref: '/api/sslprofile?name=System-Standard'
            application_profile_ref: '/api/applicationprofile?name=System-Secure-HTTP'
            ssl_key_and_certificate_refs:
                - '/api/sslkeyandcertificate?name=System-Default-Cert'
            pool_ref: '/api/pool?name=testpool2'



Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



