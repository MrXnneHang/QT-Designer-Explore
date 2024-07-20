## 1.python版本低，pyqt版本过高.

> DeprecationWarning: sipPyTypeDict() is deprecated, the extension module should use sipPyTypeDictRef() instead

https://stackoverflow.com/questions/77333277/deprecationwarning-sippytypedict-is-deprecated-pyqt5

**Solve:**降级pyqt,pyqt-tools

```cmd
pip install PyQt5==5.15.4 PyQt5-Qt5==5.15.2 PyQt5-sip==12.12.1
pip install pyqt5-tools==5.15.4.3.0.3
```

有意思的是pyqt5和pyqt5-tools的版本号都是一样的。