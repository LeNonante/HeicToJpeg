# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\Aurelien\\Documents\\PROJETS\\HEICJPG\\heic_to_jpeg02.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pillow_heif', 'tkinter', 'Pillow'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='heic_to_jpeg02',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
