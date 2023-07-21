from pylenium.driver import Pylenium 
# from pyleniumio import Pylenium

def test_google(py: Pylenium):
    py.browser = webdriver.Chrome()
    py.visit("https://google.com")
    py.get('[name="q"]').type('puppies')
    py.get('[name="btnK"]').submit()
    assert py.should().contain_title('puppies') 


test_google(Pylenium)