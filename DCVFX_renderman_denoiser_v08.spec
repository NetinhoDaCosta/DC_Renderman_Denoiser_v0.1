# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['F:/DC_programming/DC-vfx_renderman_denoiser/DCVFX_renderman_denoiser_v08.py'],
             pathex=['F:\\DC_programming\\DC-vfx_renderman_denoiser'],
             binaries=[],
             datas=[('F:/DC_programming/DC-vfx_renderman_denoiser/images', 'images/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='DCVFX_renderman_denoiser_v08',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='F:\\DC_programming\\DC-vfx_renderman_denoiser\\images\\favicon.ico')
