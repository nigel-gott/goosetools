from pathlib import Path

import pytest
import requests


def snapshot(browser, name):
    working_dir = Path().absolute()
    snapshot_path = working_dir / "misc_data" / f"{name}.html"
    browser.html_snapshot(str(snapshot_path.absolute()))


def wait_and_click(browser, element_id):
    if not browser.is_element_present_by_id(element_id, wait_time=10):
        snapshot(browser, f"cant_find_{element_id}")
        assert False
    button = browser.find_by_id(element_id).first
    button.click()


@pytest.mark.slow
def test_can_sign_up_and_create_new_fleet(http_service, browser):
    response = requests.get(http_service)
    assert response.status_code == 200

    browser.visit("http://django:8000/goosetools/accounts/discord/login/")

    wait_and_click(browser, "sign_up_button")

    browser.visit("http://django:8000/goosetools/fleet")
    wait_and_click(browser, "start_new_fleet_button")
    browser.find_by_id("id_name").first.fill("Test Fleet Name")
    wait_and_click(browser, "create_fleet_button")

    assert browser.is_text_present("Test Fleet Name", wait_time=10)
