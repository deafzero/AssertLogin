from playwright.sync_api import Page, expect


URL = "https://the-internet.herokuapp.com/login"

def test_is_page_login(page: Page) -> None : 
    page.goto(URL)
    expect(page.get_by_role("heading", name="Login Page")).to_be_visible()

# Positive test case valid login with username and password true 
def test_valid_login(page: Page)  -> None : 
    page.goto(URL)
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.locator("html.no-js body div.row div#content.large-12.columns div.example form#login button.radius").click()
    expect(page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()

def test_wrong_password(page: Page) -> None:
    page.goto(URL)
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("Falsepassword")
    page.locator("html.no-js body div.row div#content.large-12.columns div.example form#login button.radius").click()

    # Pass jika tidak berhasil login ke secure AREA
    expect(page.locator('#flash-messages')).to_contain_text("Your password is invalid! ")
        
def test_wrong_username(page: Page) -> None:
    page.goto(URL)
    page.get_by_label("Username").fill("Falsetomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.locator("html.no-js body div.row div#content.large-12.columns div.example form#login button.radius").click()

    # Pass jika tidak berhasil login ke secure AREA
    expect(page.locator('#flash-messages')).to_contain_text("Your username is invalid! ")

    
def test_case_sensitive_username(page: Page) -> None :
    page.goto(URL)
    page.get_by_label("Username").fill("TOMSMITH")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.locator("html.no-js body div.row div#content.large-12.columns div.example form#login button.radius").click()

    # Pass jika tidak berhasil login ke secure AREA
    expect(page.locator('#flash-messages')).to_contain_text("Your username is invalid! ")

def test_case_sensitive_password(page: Page) -> None :
    page.goto(URL)
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SUPERSECRETPASSWORD!")
    page.locator("html.no-js body div.row div#content.large-12.columns div.example form#login button.radius").click()

    # Pass jika tidak berhasil login ke secure AREA
    expect(page.locator('#flash-messages')).to_contain_text("Your password is invalid! ")

    
    

if __name__  == "__main__" : 
    # test_main()
    ...