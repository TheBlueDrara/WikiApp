import pytest
from ShibariWiki import app, collection


# Test if the home page returns a 200 status code
def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200


# Test if the add item page returns a 200 status code
def test_add_item_page():
    client = app.test_client()
    response = client.get('/add')
    assert response.status_code == 200


# Test if the filter page returns a 200 status code
def test_filter_page():
    client = app.test_client()
    response = client.get('/filter')
    assert response.status_code == 200


# Test if adding an item works
def test_add_item():
    client = app.test_client()

    # Valid data
    response = client.post('/add', data=dict(
        tie_name='Test Tie',
        description='Test Description',
        length_of_rope=8,
        rope_type='yuta',
        amount_of_ropes_needed=2
    ), follow_redirects=True)

    # Print the content of the response for debugging
    print(response.data)

    assert b'Technique Added Successfully!' in response.data  # Check if the success message is in the response HTML content

    # Invalid data (missing tie_name)
    response = client.post('/add', data=dict(
        description='Test Description',
        length_of_rope=8,
        rope_type='yuta',
        amount_of_ropes_needed=2
    ))
    assert response.status_code == 400

    # Clean up: remove the added item
    collection.delete_one({"tie_name": 'Test Tie'})




# Test if filtering techniques works with different filters
def test_filter_techniques():
    client = app.test_client()

    # Filter by available rope
    response = client.get('/filter?available_rope=5&rope_length=10&filter_rope_type=')
    assert response.status_code == 200

    # Filter by rope length
    response = client.get('/filter?available_rope=&rope_length=10&filter_rope_type=')
    assert response.status_code == 200

    # Filter by rope type
    response = client.get('/filter?available_rope=&rope_length=&filter_rope_type=yuta')
    assert response.status_code == 200

    # Filter by combination of all criteria
    response = client.get('/filter?available_rope=5&rope_length=10&filter_rope_type=yuta')
    assert response.status_code == 200


# Test if deleting an item works
def test_delete_item():
    client = app.test_client()

    # Add a test item
    collection.insert_one({
        "tie_name": "Test Tie",
        "description": "Test Description",
        "length_of_rope": 8,
        "rope_type": "yuta",
        "amount_of_ropes_needed": 2
    })

    # Get the ID of the test item
    test_item = collection.find_one({"tie_name": "Test Tie"})

    # Try to delete the test item
    response = client.post(f'/delete_item/{test_item["tie_name"]}', follow_redirects=True)
    assert b'Item deleted successfully' in response.data


# Test if displaying a technique works
def test_display_technique():
    client = app.test_client()

  
