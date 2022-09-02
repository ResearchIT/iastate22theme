from django.apps import AppConfig

class MenuItem(object):
    def __init__(self, text, url, children=None):
        self.text = text
        self.url = url
        if children is None:
            children = []
        self.children = children

class SocialMenuItem(MenuItem):
    def __init__(self, text, url, icon=None):
        self.text = text
        self.url = url
        self.children = []
        self.icon = icon

class Iastate22ThemeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iastate22theme'
    html_title_tag = 'IASTATE22 Site Page Title'
    header_parent_unit_name = 'IASTATE22 Parent Unit Name'
    header_parent_unit_url = '#'
    header_site_title = 'IASTATE22 Site Title'
    footer_site_title = 'IASTATE22 Site Name/Org Name Lorem Ipsum'
    menu = [
        MenuItem("Dropdown Menu", "/features", [
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Submenu", "#", [
                MenuItem("Level 3 Submenu", "#", [
                    MenuItem("Level 4 Page", "#"),
                    MenuItem("Level 4 Page", "#"),
                ]),
                MenuItem("Level 3 Page", "#"),
            ]),
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Page", "#")
        ]),
        MenuItem("Link", "#")
    ]
    header_site_links_menu = [
        MenuItem("Sign Ons and Tools", "https://login.iastate.edu/"),
    ]
    footer_primary_links_menu = [
        MenuItem("Sign Ons and Tools", "https://login.iastate.edu/"),
    ]
    footer_secondary_links_menu = [
        MenuItem("Sign Ons and Tools", "https://login.iastate.edu/"),
    ]
    footer_social_media_menu = [
        SocialMenuItem("Facebook", "http://facebook.com/IowaStateU/", "fa-brands fa-facebook"),
        SocialMenuItem("Twitter", "http://twitter.com/iowastateu?lang=en", "fa-brands fa-twitter"),
        SocialMenuItem("Instagram", "http://instagram.com/iowastateu/", "fak fa-iastate22-instagram"),
        SocialMenuItem("YouTube", "http://youtube.com/user/iowastateu", "fa-brands fa-youtube"),
        SocialMenuItem("LinkedIn", "http://linkedin/iowastateu?lang=en", "fa-brands fa-linkedin-in"),
    ]

    footer_contact_address = """
        Building<br>
        12345 Street Address<br>
        Ames, IA 50011
    """

    footer_contact_email = "email@iastate.edu"
    footer_contact_phone = "(515) 294-4347"
