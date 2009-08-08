## Script (Python) "get_plone_version"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
version = context.portal_migration.getInstanceVersion().split('.')
ver = (version[0] + version[1])[:2]
if ver == '31':
    ver = '30'
elif ver == '33':
    ver = '32'
return ver
