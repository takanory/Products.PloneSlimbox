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
if ver == '31':
    ver = '30'
elif ver == '33':
    ver = '32'
elif ver == '41':
    ver = '40'
return ver
