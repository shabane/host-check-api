# Host Check API

This is an API endpoint to check an *host:port* is avilable
or not. its intentinal to use on data centers in countries
like iran for check the restriction of internet.


### Usage Example

```bash
curl http://127.0.0.1:8000/api/tcp?host=google.com&port=443&timeout=1
```

|       HTTP parameter      |           Explain      |       Requre      |
|:-------------------------:|:----------------------:|:-----------------:|
|           host            |  the host ip or domain |        True       |
|           port            |  the host port         |        True       |
|          timeout          |  expire time to check  |        False      |
