# checkin

wget https://gh-proxy.com/https://raw.githubusercontent.com/awhao/checkin/main/Shell/api_fast_cn.sh -O api_fast_cn.sh -cwd script/Shell
sh script/Shell/api_fast_cn.sh
apk add bash git
git clone https://gh-proxy.com/https://github.com/awhao/checkin 

chmod +x ins_pkg.sh && bash ins_pkg.sh -cwd script/Shell -timeout 0

chmod +x ins_pkg.sh && bash ins_pkg.sh 
chmod +x ins_selenium.sh && bash ins_selenium.sh 


sh "$(curl -fsSL https://gh-proxy.com/https://raw.githubusercontent.com/awhao/checkin/main/Shell/api_fast_cn.sh | sh)"