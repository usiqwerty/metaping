# metaping

Advanced host availability checker

## Usage

```shell
metaping google.com
```

Will try to access `google.com` with following methods (in order of priority):

1. HTTPS
2. HTTP
3. ICMP ping
