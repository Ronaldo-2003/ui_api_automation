from api.api_client import APIClient
from pages.users_page import UsersPage

def test_user_flow_ui_api(driver):
    # API step – backend setup
    api = APIClient()
    response = api.create_user()
    assert response.status_code == 201

    # UI step – frontend validation
    driver.get("https://the-internet.herokuapp.com/tables")

    users_page = UsersPage(driver)
    rows = users_page.get_rows()

    assert len(rows) > 0
