import PyInstaller.__main__

PyInstaller.__main__.run([
    'finance_yahoo_info.py',
    '--onefile',
    '--clean'
])
