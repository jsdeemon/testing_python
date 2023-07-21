from Pylenium.driver import Pylenium 


class TodoPage:
    def __init__(self, py: Pylenium):
        self.py = py 

    def goto(self):
        self.py.visit("https://lambdatest.github.io/sample-todo-app")
        return self


def test_check_first_item(py:Pylenium):
    py.visit("https://lambdatest.github.io/sample-todo-app")
    # 2. get the checkbox
    # find in console by xpath: $x("//*[text()='First Item']")[0]
    # $x("//*[text()='First Item']")[0].parentElement.querySelector('input').click()
    checkbox = py.getx("//*[text()='First Item']").parent().get('input')
    # 3. click it
    checkbox.click()
    # 4.assert that is checked
    assert checkbox.should().be_checked() 

def test_check_many_items(py: Pylenium):
    py.visit("https://lambdatest.github.io/sample-todo-app")

    # $$("li[ng-repeat*='sampletodo']")
    todos = py.find("li[ng-repeat*='sampletodo']")
    todo2, todo4 = todos[1], todos[3]
    todo2.get('input').click()
    todo4.get('input').click()
    assert py.contains("3 of 5 remaining")