block_cipher = None

import os

a = Analysis(['main.pyw'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[],
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

from const import *

a.datas += [('joker.png',JOKER_IMG_PATH, 'DATA')]
a.datas += [('monero.png',MONERO_IMG_PATH, 'DATA')]
a.datas += [('key.png',KEY_IMG_PATH, 'DATA')]
a.datas += [('bouffon.ico',BUFFOON_ICO_PATH, 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=EXE_NAME,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon=BUFFOON_ICO_PATH)