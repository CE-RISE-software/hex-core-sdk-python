# CE-RISE Python SDK for Hexagonal Core Service

[![DOI](https://zenodo.org/badge/DOI/TOBEOBTAINED.svg)](https://doi.org/TOBEOBTAINED)

Python SDK for the CE-RISE Hex Core Service:
https://codeberg.org/CE-RISE-software/hex-core-service

## Install

Install from PyPI:

```bash
pip install ce-rise-hex-core-sdk
```

Install a specific version:

```bash
pip install "ce-rise-hex-core-sdk==0.0.0.dev120"
```

## Quickstart

### 1) Configure client and call public endpoints

```python
import ce_rise_hex_core_sdk as hexsdk

config = hexsdk.Configuration(host="http://localhost:8080")

with hexsdk.ApiClient(config) as client:
    admin_api = hexsdk.AdminApi(client)
    discovery_api = hexsdk.DiscoveryApi(client)

    health = admin_api.health()
    models = discovery_api.list_models()

    print("health:", health.status)
    print("models:", models)
```

### 2) Configure bearer token for protected endpoints

```python
import os
import ce_rise_hex_core_sdk as hexsdk

config = hexsdk.Configuration(
    host="http://localhost:8080",
    access_token=os.environ["BEARER_TOKEN"],
)
```

### 3) Validate and create records

```python
import ce_rise_hex_core_sdk as hexsdk

config = hexsdk.Configuration(
    host="http://localhost:8080",
    access_token="<jwt-token>",
)

with hexsdk.ApiClient(config) as client:
    models_api = hexsdk.ModelsApi(client)

    report = models_api.validate_model_payload(
        model="re-indicators-specification",
        version="0.0.3",
        validate_request=hexsdk.ValidateRequest(payload={"example": "value"}),
    )

    record = models_api.create_record(
        model="re-indicators-specification",
        version="0.0.3",
        idempotency_key="my-unique-request-id-001",
        create_request=hexsdk.CreateRequest(payload={"example": "value"}),
    )

    print("validation passed:", report.passed)
    print("record id:", record.id)
```

## API Documentation

- Generated docs website: https://ce-rise-software.codeberg.page/hex-core-sdk-python/
- Local API docs:
  - `docs/AdminApi.md`
  - `docs/DiscoveryApi.md`
  - `docs/ModelsApi.md`

## License

Licensed under the [European Union Public Licence v1.2 (EUPL-1.2)](LICENSE).

## Contributing

This repository is maintained on [Codeberg](https://codeberg.org/CE-RISE-software/hex-core-sdk-python) as the canonical source of truth. The GitHub repository is a read-only mirror used for release archival and Zenodo integration.

---

<a href="https://europa.eu" target="_blank" rel="noopener noreferrer">
  <img src="https://ce-rise.eu/wp-content/uploads/2023/01/EN-Funded-by-the-EU-PANTONE-e1663585234561-1-1.png" alt="EU emblem" width="200"/>
</a>

Funded by the European Union under Grant Agreement No. 101092281 - CE-RISE.  
Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the granting authority (HADEA). Neither the European Union nor the granting authority can be held responsible for them.

(c) 2026 CE-RISE consortium.  
Licensed under the [European Union Public Licence v1.2 (EUPL-1.2)](LICENSE).  
Attribution: CE-RISE project (Grant Agreement No. 101092281) and the individual authors/partners as indicated.

<a href="https://www.nilu.com" target="_blank" rel="noopener noreferrer">
  <img src="https://nilu.no/wp-content/uploads/2023/12/nilu-logo-seagreen-rgb-300px.png" alt="NILU logo" height="20"/>
</a>

Developed by NILU (Riccardo Boero - ribo@nilu.no) within the CE-RISE project.
