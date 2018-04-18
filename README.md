# python-skeleton-gdal-hello-only

This is a simple endpoint to test the CPU overhead/size of the conda installation on a Debian Jessie-Slim base.

It does not do any geometry calculations, and doesn't import any heavy packages (ogr, numpy, pandas etc).

Regardless of payload, it will return:
{
    "dissolve": "ok"
}

### Endpoint
Please send POST requests to: /v1/test-gdal-hello/dissolve

### Payload
No payload is required.

### Development
1. Run the ms.sh shell script in development mode.

```ssh
./ps.sh develop
```
