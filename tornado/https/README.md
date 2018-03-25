##使用oepnssl生成server.key和server.crt的步骤

### 1. 生成key

​	需要输入至少4位数的密码

```
openssl genrsa -des3 -out server.key 2048
```

### 2. 生成无密码版key

```
openssl rsa -in server.key -out server.key
```

### 3. 生成ca.crt

```
openssl req -new -x509 -key server.key -out ca.crt -days 3650 
```

### 4. 生成server.csr

```
openssl req -new -key server.key -out server.csr 
```

### 5. 生成server.crt

```
openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
```

