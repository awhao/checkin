# checkin

wget https://gh-proxy.com/https://raw.githubusercontent.com/awhao/checkin/main/elecv2p/shell/api_fast_cn.sh -O api_fast_cn.sh -cwd script/Shell
sh script/Shell/api_fast_cn.sh
apk add bash git
git clone https://gh-proxy.com/https://github.com/awhao/checkin script/Shell

chmod +x ins_pkg.sh && bash ins_pkg.sh -cwd script/Shell -timeout 0