# conftest.py
import pytest_html
import pytest
def pytest_configure(config):
    #config._metadata['Project Name'] = 'SauceDemo Testing'
    #config._metadata['Test Environment'] = 'Staging'
    #config._metadata['Tester'] = 'Meghana Rao'
    pass

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.append(pytest_html.extras.text("Custom Summary Section"))
