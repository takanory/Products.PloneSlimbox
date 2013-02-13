## Script (Python) "get_plone_version"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
try:
  version = context.portal_migration.getSoftwareVersion().split('.')
except:
  version = context.portal_migration.getInstanceVersion().split('.')
ver = (version[0] + version[1])[:2]

try:
    int_ver = int(ver)
except ValueError:
    return ver

available = [40, 32, 30, 25, 21]
for av in available:
    if int_ver >= av:
        return str(av)

return ver
