import sys

if ('debugpy' in sys.modules \
       and sys.modules['debugpy'].__file__.find('/.vscode/extensions/') > -1):
    print("Running in VS Code debug")
else:
    print("Not in VS code debug")