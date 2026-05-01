# python-port-scanner-pro.
A Python-based network utility for identifying open ports and service banners.
# Python Port Scanner

## Objective
A visceral network probing tool designed to identify open TCP ports and perform service banner grabbing to determine the identity of running services.

## Methodology
The script utilises the `socket` library to attempt a full TCP handshake. If successful, it sends a probe byte string to induce a response from the service.

## Usage
```bash
python scanner.py
