"""Tests for TextMVP."""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_startup():
    resp = client.post("/process", json={"text": "test", "operation": "upper"})
    assert resp.status_code == 200

def test_uppercase():
    resp = client.post("/process", json={"text": "hello", "operation": "upper"})
    assert resp.json()["result"] == "HELLO"

def test_lowercase():
    resp = client.post("/process", json={"text": "HELLO", "operation": "lower"})
    assert resp.json()["result"] == "hello"

def test_reverse():
    resp = client.post("/process", json={"text": "abcd", "operation": "reverse"})
    assert resp.json()["result"] == "dcba"

def test_empty_text():
    resp = client.post("/process", json={"text": "   ", "operation": "upper"})
    assert resp.status_code == 400

def test_invalid_operation():
    resp = client.post("/process", json={"text": "hi", "operation": "invalid"})
    assert resp.status_code == 400
