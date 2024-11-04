# checkin

## 配置文件

青龙面板点击左侧配置文件,右上角选择config.sh，更改下面这行

```sh
## ql repo命令拉取脚本时需要拉取的文件后缀，直接写文件后缀名即可
RepoFileExtensions="js mjs py pyc sh toml"
```

根据推送需求更改config.sh文件，或者在设置中配置推送方式

## 依赖管理

Linux -> 创建依赖 -> 修改名称为

```sh
bash curl gcc g++ make libffi-dev openssl-dev
```

Python3 -> 创建依赖 -> 修改名称为

```sh
bs4 cryptography dateparser feedparser peewee pyaes pyppeteer requests rsa schedule tomli
```

## 拉取仓库

```sh
ql repo https://github.com/awhao/checkin.git "api_|ck_" "^checkin|ins_" "^notify|^utils|check" "main"
```

## 修改toml


## 感谢

* [qinglong](https://github.com/whyour/qinglong)
* [checkinpanel](https://github.com/OreosLab/checkinpanel)
* [elecV2P](https://github.com/elecV2/elecV2P)
  