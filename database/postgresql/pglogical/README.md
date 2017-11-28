安装步骤:
sudo apt-get install libselinux-dev libpam-dev libedit-dev -y
sudo apt install postgresql-server-dev-9.4

git clone https://github.com/2ndQuadrant/pglogical.git
git submodule update --init --recursive
make USE_PGXS=1
sudo make USE_PGXS=1 install