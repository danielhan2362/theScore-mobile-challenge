from appium.webdriver.common.appiumby import AppiumBy


class Onboarding:
    GET_STARTED_BUTTON = (AppiumBy.ID, 'com.fivemobile.thescore:id/btn_primary')
    CCPA_CONTINUE_BUTTON = (AppiumBy.ID, 'com.fivemobile.thescore:id/accept_button')
    NFL_FOOTBALL_ROW = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/txt_name\" and @text=\"NFL Football\"]')
    SF_NINERS = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/txt_name\" and @text=\"San Francisco 49ers\"]")
    CONTINUE_BUTTON = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")
    MAYBE_LATER = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_secondary")


class HomeScreen:
    OK_GOT_IT = (AppiumBy.XPATH, '//android.view.View[@content-desc=\"Ok, Got It\"]')
    LEAGUES_TAB = (AppiumBy.ID, "com.fivemobile.thescore:id/navigation_leagues")


class LeaguesScreen:
    LEAGUE_SCREEN_TITLE = (AppiumBy.ID, 'com.fivemobile.thescore:id/titleTextView')
    EDIT = (AppiumBy.ID, "com.fivemobile.thescore:id/header_right_text")
    DONE = (AppiumBy.ID, "com.fivemobile.thescore:id/header_right_text")
    NFL_ROW = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id=\"com.fivemobile.thescore:id/league_name_text\" and @text=\"NFL\"]")


class NFLScreen:
    STANDINGS_TAB = (AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc=\"Standings\"]")
    AFC_TAB = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"AFC\"]")
