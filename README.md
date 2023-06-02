# 安装
## 安装pip

检测是否安装 `pip`:
```shell
pip --version
```

安装 `pip`
```shell
sudo python3 get-pip.py
```

## 在OS X系统中安装Pygame

要安装Pygame依赖的有些包，需要Homebrew。

### 安装Homebrew

[Homebrew](https://brew.sh/) 依赖于Apple包Xcode，因此请打开一个终端窗口并执行如下命令:
```shell
xcode-select --install
```
在不断出现的确认对话框中都单击OK按钮。

安装 Homebrew：
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### 安装Pygame依赖的库

安装运行游戏所需的库:

```shell
brew install hg sdl sdl_image sdl_ttf
```

安装高级功能如声音等所需的库：

```shell
brew install sdl_mixer portmidi
```

### 安装Pygame

```shell
pip3 install --user hg+http://bitbucket.org/pygame/pygame
```

检查是否安装成功：
```shell
$ python3
>>> import pygame
pygame 2.3.0 (SDL 2.24.2, Python 3.10.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
```

导入 pygame 后成功输出如上信息，表明安装成功