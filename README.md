# Veriflow

Verify torrent safety before download

# TextMVP

A minimal text processing service using FastAPI.

## Usage

Run the server:
uvicorn main:app --reload

## API

POST /process
Body: {"text": "string", "operation": "upper|lower|reverse|words"}

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[Client] -->|POST /process| B(FFastAPI App)
    B -->|Validate| C{Pydantic Model}
    C -->|Valid| D[Process Text]
    C -->|Invalid| E[400 Error]
    D -->|Transform| F[Result + Metadata]
    F -->|JSON| A
```

</details>
