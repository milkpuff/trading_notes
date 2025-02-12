+++
date = '2025-01-25T02:12:58+08:00'
draft = true
title = 'Cloudflare转发samba'
author = 'Puff'
+++

### Cloudflare 新建Zero Trust

添加公共主机名 public hostname

### server 配置Cloudflare 服务

### client 启动 Cloudflare

```
cloudflared access tcp --hostname smb.sunbana.art --url localhost:8445
```

### smbclient

```
smbclient //127.0.0.1/public --port=8445 -U username%passwd
```

### 挂载

```
sudo mount -t cifs //127.0.0.1/public ./test -o username=puff,password=passwd,uid=1000,gid=1000,port=8445
```
