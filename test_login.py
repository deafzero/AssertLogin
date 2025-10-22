from playwright.sync_api import sync_playwright, expect

def test_main() -> None : 
    with sync_playwright() as p :
        ff_browser = p.firefox.launch()
        page = ff_browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        expect(page.get_by_role("heading", name='Login Page')).to_be_visible()
        ff_browser.close()
        
    
    

if __name__  == "__main__" : 
    # test_main()
    ...