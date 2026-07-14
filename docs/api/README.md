# AEON MATRIX API Documentation

## Swagger UI

Open:

/swagger-ui.html


## API Specification

OpenAPI 3.0.3

## Core Services

### Telemetry Ingestion
POST /api/v1/events

รับ Event จาก WMS, GPS, IoT และ Transport System


### AI Intelligence Engine
POST /api/v1/ai/analyze

วิเคราะห์ Event ด้วย AI Decision Engine


## Event Types

- ORDER_CREATED
- GPS_UPDATED
- STOCK_SHORTAGE
- POLICY_VIOLATION
- ETA_RISK
