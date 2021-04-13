# Install_AWX

### git clone
```
# git clone https://github.com/yahanjunho/Install_AWX.git
```


### prerequirment for docker, docker-compose
```
1) remove, default docker packages
# yum remove -y docker \
                docker-client \
                docker-client-latest \
                docker-common \
                docker-latest \
                docker-latest-logrotate \
                docker-logrotate \
                docker-engine \
                docker-ce \
                docker-ce-cli \
                containerd.io
                
2) install, prerequirement packages for docker
# yum install -y yum-utils device-mapper-persistent-data lvm2

3) install, docker
# yum install -y docker-ce docker-ce-cli containerd.io

4) enable, start docker daemon
# systemctl enable docker
# systemctl start docker

5) install, prerequirment packages for docker-compose
# pip install docker docker-compose

6) install, docker-compose
# yum install -y docker-compose
```
  
### mv awxdb_version /opt/awxdb_version, mv awxcompose_version /opt/awxcompose_version
```
# cd Install_AWX
# cp -rfp awxdb/awxdb_version /opt/awxdb_version
# cp -rfp awxcompose/awxcompose_version /opt/awxcompose_version
```


### docker-compose up -d
```
# cd /opt/awxcompose_version
# docker-compose up -d
```
  
<br>
<br>

## If you want to make docker-compose.yml directly, Follow below
### check, ansible's python interpreter version (ansible must be installed with python 2.X)
```
# ansible --version
ansible 2.9.17
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible
  python version = 2.7.5 (default, Oct 14 2020, 14:45:30) [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
```

```
# which python
/usr/bin/python
```

### check, extra_vars
```
awx_version : awx's version which want to be installed (ex, 9.1.1)
python_path : 'which python' command's result (ex, /usr/bin/python )
docker_installation : 'y' is that install also docker + docker-compose / 'n' is that do not install any docker + docker-compose
```

> check tag in ansible/awx github's repository - [https://github.com/ansible/awx](https://github.com/ansible/awx)  

```
# ansible-playbook progress_public_awx_install.yml -e "awx_version=9.1.1 docker_installation=n python_path=/usr/bin/python"
```
