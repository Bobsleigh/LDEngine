# Fichier pour générer l'application autonome Darwin
# Pour lancer la création des binaires :
#        OSX : pyinstaller --onefile mainOSX.spec
# le résultat se trouve dans /dist -> mainOSX
# Note de Thomas : chez moi, la variable pathex ne sert à rien...
# si je la retire, tout fonctionne correctement, j'attends des retours
# windowsiens là dessus. Si je dis vrai, personne n'aura rien à éditer !
#
# Note : Il faut que xquartz  soit installé sur mac pour que ça marche.
#        (https://www.xquartz.org)
#

block_cipher = None

addedFiles = [ ('tiles_map', 'tiles_map'), ('music','music'), ('img', 'img')]

a = Analysis(['main.py'],
             #pathex=['LDEngine'],
             binaries=None,
             datas=addedFiles,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main_binaire',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='mainOSX.app',
             icon=None,
             bundle_identifier=None)