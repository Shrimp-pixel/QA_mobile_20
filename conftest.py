import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import wikipedia_mobile.utils.selene.patch_selector_strategy  # noqa
    import wikipedia_mobile.utils.selene.patch_element_mobile_commands  # noqa
