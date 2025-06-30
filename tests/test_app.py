import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test that home page loads successfully"""
    rv = client.get('/')
    assert rv.status_code == 200

def test_product_listing(client):
    """Test product listing page"""
    rv = client.get('/products')
    assert rv.status_code in [200, 302]  # 302 if redirect to login