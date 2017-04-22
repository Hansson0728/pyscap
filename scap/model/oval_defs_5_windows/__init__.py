# Copyright 2016 Casey Jaymes

# This file is part of PySCAP.
#
# PySCAP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PySCAP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PySCAP.  If not, see <http://www.gnu.org/licenses/>.
TAG_MAP = {
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_test': 'AccessTokenTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_test': 'ActiveDirectory57TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_test': 'ActiveDirectoryTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_test': 'AuditEventPolicySubcategoriesTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_test': 'AuditEventPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_test': 'CmdletTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_test': 'DnsCacheTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_test': 'FileAuditedPermissions53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_test': 'FileAuditedPermissionsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_test': 'FileEffectiveRights53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_test': 'FileEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_test': 'FileTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_test': 'GroupSidTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_test': 'GroupTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_test': 'InterfaceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_test': 'LicenseTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_test': 'LockoutPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_test': 'MetabaseTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_test': 'NtUserTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_test': 'PasswordPolicyTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_test': 'PeHeaderTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_test': 'PortTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_test': 'PrinterEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_test': 'Process58TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_test': 'ProcessTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_test': 'RegistryTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_test': 'RegKeyAuditedPermissions53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_test': 'RegKeyAuditedPermissionsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_test': 'RegKeyEffectiveRights53TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_test': 'RegKeyEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_test': 'ServiceEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_test': 'ServiceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_test': 'SharedResourceAuditedPermissionsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_test': 'SharedResourceEffectiveRightsTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_test': 'SharedResourceTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_test': 'SidSidTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_test': 'SidTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_test': 'SystemMetricTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_test': 'UacTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_test': 'UserRightTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_test': 'UserSid55TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_test': 'UserSidTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_test': 'UserTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_test': 'VolumeTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_test': 'Wmi57TestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_test': 'WmiTestElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_test': 'WuaUpdateSearcherTestElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_object': 'AccessTokenObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_object': 'ActiveDirectory57ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_object': 'ActiveDirectoryObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_object': 'AuditEventPolicySubcategoriesObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_object': 'AuditEventPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_object': 'CmdletObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_object': 'DnsCacheObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_object': 'FileAuditedPermissions53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_object': 'FileAuditedpermissionsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_object': 'FileEffectiveRights53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_object': 'FileEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_object': 'FileObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_object': 'GroupSidObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_object': 'GroupObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_object': 'InterfaceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_object': 'LicenseObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_object': 'LockoutPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_object': 'MetabaseObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_object': 'NtUserObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_object': 'PasswordPolicyObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_object': 'PeHeaderObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_object': 'PortObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_object': 'PrinterEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_object': 'Process58ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_object': 'ProcessObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_object': 'RegistryObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_object': 'RegKeyAuditedPermissions53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_object': 'RegKeyAuditedPermissionsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_object': 'RegKeyEffectiveRights53ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_object': 'RegKeyEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_object': 'ServiceEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_object': 'ServiceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_object': 'SharedResourceAuditedPermissionsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_object': 'SharedResourceEffectiveRightsObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_object': 'SharedResourceObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_object': 'SidSidObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_object': 'SidObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_object': 'SystemMetricObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_object': 'UacObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_object': 'UserRightObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_object': 'UserSid55ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_object': 'UserSidObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_object': 'UserObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_object': 'VolumeObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_object': 'Wmi57ObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_object': 'WmiObjectElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_object': 'WuaUpdateSearcherObjectElement',

    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}accesstoken_state': 'AccessTokenStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory57_state': 'ActiveDirectory57StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}activedirectory_state': 'ActiveDirectoryStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicysubcategories_state': 'AuditEventPolicySubcategoriesStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}auditeventpolicy_state': 'AuditEventPolicyStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}cmdlet_state': 'CmdletStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}dnscache_state': 'DnsCacheStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions53_state': 'FileAuditedPermissions53StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileauditedpermissions_state': 'FileAuditedpermissionsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights53_state': 'FileEffectiveRights53StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}fileeffectiverights_state': 'FileEffectiveRightsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}file_state': 'FileStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_sid_state': 'GroupSidStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}group_state': 'GroupStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}interface_state': 'InterfaceStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}license_state': 'LicenseStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}lockoutpolicy_state': 'LockoutPolicyStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}metabase_state': 'MetabaseStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}ntuser_state': 'NtUserStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}passwordpolicy_state': 'PasswordPolicyStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}peheader_state': 'PeHeaderStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}port_state': 'PortStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}printereffectiverights_state': 'PrinterEffectiveRightsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process58_state': 'Process58StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}process_state': 'ProcessStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}registry_state': 'RegistryStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions53_state': 'RegKeyAuditedPermissions53StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyauditedpermissions_state': 'RegKeyAuditedPermissionsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights53_state': 'RegKeyEffectiveRights53StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}regkeyeffectiverights_state': 'RegKeyEffectiveRightsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}serviceeffectiverights_state': 'ServiceEffectiveRightsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}service_state': 'ServiceStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceauditedpermissions_state': 'SharedResourceAuditedPermissionsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresourceeffectiverights_state': 'SharedResourceEffectiveRightsStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sharedresource_state': 'SharedResourceStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_sid_state': 'SidSidStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}sid_state': 'SidStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}systemmetric_state': 'SystemMetricStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}uac_state': 'UacStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}userright_state': 'UserRightStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid55_state': 'UserSid55StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_sid_state': 'UserSidStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}user_state': 'UserStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}volume_state': 'VolumeStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi57_state': 'Wmi57StateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wmi_state': 'WmiStateElement',
    '{http://oval.mitre.org/XMLSchema/oval-definitions-5#windows}wuaupdatesearcher_state': 'WuaUpdateSearcherStateElement',
}
