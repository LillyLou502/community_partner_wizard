# get the CP database
import re
import os

class CommunityPartner():
    # create a dictionary inside the class
    def __init__(self, org, contact, phone, email, web, primary_issue, special_issue):
        self.org = org
        self.contact = contact
        self.phone = phone
        self.email = email
        self.web = web
        self.primary_issue = primary_issue
        self.special_issue = special_issue

@property
def CP_dict(self):
    return {"Organization": self.org,
            "Contac Name": self.contact,
            "Phone Number": self.phone,
            "Email Address": self.email,
            "Web Address": self.web,
            "Select Primary Social Justice Issues (check all that apply)": self.primary_issue,
            "In your own words, describe the social issues your organization addresses:": self.special_issue}

def create():
    # allow user to add to CP

def read():
    # allow user to look up a CP by org or issue

def update():
    # allow user to change info in CP

def delete():
    # allow user to delete CP