from django.apps import AppConfig

class MenuItem(object):
    def __init__(self, text, url, newtab=False, children=None):
        self.title = text
        self.url = url
        if children is None:
            children = []
        self.children = children
        self.newtab = newtab

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
    parent_unit = {
        "name": "IASTATE22 Parent Unit Name",
        "url": "#"
    }
    website_title = {
        "text": "IASTATE22 Site Title",
        "url": "/"
    }
    footer_site_title = 'IASTATE22 Site Name/Org Name Lorem Ipsum'
    full_nav = [
        MenuItem("Dropdown Menu", "/features", False, [
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Page", "#"),
            MenuItem("Level 2 Page", "#")
        ]),
        MenuItem("Link", "#")
    ]
    search_visible = True
    utility_button = None
    #utility_button = MenuItem("Button text", "#")
    utility_nav = [
        MenuItem("Info For...", "#", False, [
            MenuItem("Current Students", "https://students.info.iastate.edu/"),
            MenuItem("Faculty and Staff", "https://facultystaff.info.iastate.edu/")
        ]),
        MenuItem("Sign Ons", "https://login.iastate.edu/"),
    ]
    social_links = [
        SocialMenuItem("Facebook", "http://facebook.com/IowaStateU/", "fa-brands fa-facebook"),
        SocialMenuItem("Twitter", "http://twitter.com/iowastateu?lang=en", "fa-brands fa-twitter"),
        SocialMenuItem("Instagram", "http://instagram.com/iowastateu/", "fak fa-iastate22-instagram"),
        SocialMenuItem("YouTube", "http://youtube.com/user/iowastateu", "fa-brands fa-youtube"),
        SocialMenuItem("LinkedIn", "http://linkedin/iowastateu?lang=en", "fa-brands fa-linkedin-in"),
    ]
    footer_nav = [
        MenuItem("Footer Nav Item 1", "#"),
        MenuItem("Footer Nav Item 2", "#"),
        MenuItem("Footer Nav Item 3", "#"),
        MenuItem("Footer Nav Item 4", "#"),
    ]
    footer_secondary_nav = [
        MenuItem("Footer Secondary Nav Item 1", "#"),
        MenuItem("Footer Secondary Nav Item 2", "#"),
        MenuItem("Footer Secondary Nav Item 3", "#"),
        MenuItem("Footer Secondary Nav Item 4", "#"),
    ]
    footer_utility_nav = [
        MenuItem("Privacy Policy", "https://www.iastate.edu/disclaimers-and-terms"),
        MenuItem("Non-discrimination Policy", "https://www.policy.iastate.edu/policy/discrimination"),
        MenuItem("Digital Access and Accessibility", "https://www.digitalaccess.iastate.edu/"),
        MenuItem("Consumer Information", "https://www.iastate.edu/consumer-information"),
    ]

    site_org_contact = {
        "name": "Site Org Contact Name",
        "address": {
            "building": "Building",
            "street": "Street",
            "city_state_zip": "Ames, IA 50011"
        },
        "phone": [
            {
                "label": "Phone Label",
                "phone_number": "555-555-5555"
            },
        ],
        "email": [
            {
                "label": "Email Label",
                "email_address": "example@example.com"
            },
        ]
    }

    copyright = "Iowa State University of Science and Technology"
