# NekoBot_Plugins_Example

这是一个NekoBot插件的示例,开发者可以使用此仓库作为模板来开发自己的插件.

## 如何使用

```bash
git clone https://github.com/OfficialNekoTeam/nekobot_plugin_template.git
cd nekobot_plugin_template
```

随后修改 `metadata.yaml` 和 `main.py` 来开发自己的插件

## 安装

```bash

cd /path/data/plugins (这里的*path*指NekoBot目录)
git clone https://github.com/OfficialNekoTeam/nekobot_plugin_template.git
cd nekobot_plugin_template
pip install -r requirements.txt
```

### 插件架构

```text
   NekoBot_Plugins_Example
    ├── main.py（插件主程序包含注册插件命令 与版本等）
    ├── requirements.txt(插件需要的依赖)
    ├── metadata.yaml(插件元数据 包含插件名称 版本 描述 作者 插件仓库地址)
    └── README.md（插件自述文件）
```

---

### 插件开发

[NekoBot插件开发文档](https://docs.nekolook.com/plugins/intro)

### 插件商店

[NekoBot插件商店](https://store.nekolook.com)

### 插件提交

[NekoBot插件提交](https://store.nekolook.com/plugins/publish)
