from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout

def hidden_layout(layout):
    """隐藏布局及其子控件

    layout: QVBoxLayout/QHBoxLayout ,可以传入列表

    hidden_layout(Layout1)
    hidden_layout([Layout1,Layout2])
    """
    if isinstance(layout, list):
        for i in range(layout):
            hidden_layout(i)
    for i in range(layout.count()):  # 遍历子控件
        item = layout.itemAt(i)
        if isinstance(item, QVBoxLayout) or isinstance(item, QHBoxLayout):  # 检查是否为QLayoutItem
            hidden_layout(item)
        else:
            widget = item.widget()  # 获取子控件
            widget.setVisible(False)  # 递归调用隐藏子布局

def switch_tab_index(TabWidget,index):
    TabWidget.setCurrentIndex(index-1)