# get the CP database
import csv
import re
import os

class CommunityPartner():
    # create a dictionary inside the class
    def __init__(self):
        pass

    @property
    def CP_dict(self):
        return {"Organization": self.org,
                "Contact Name": self.contact,
                "Phone Number": self.phone,
                "Email Address": self.email,
                "Web Address": self.web,
                "Primary Issue": self.primary_issue,
                "Special Issue": self.special_issue}

    def command(self):
        command = input("What do you want to do in the Community Partner Database? Choose: create, read, update, or delete:   ")
        if command == "create":
            org = input("Organization Name:  ")
            contact = input("Contact Name:  ")
            phone = input("Contact Phone:  ")
            email = input("Contact Email:  ")
            web = input("Org Web Address:  ")
            primary_issue = input("What is your Primary Social Issue " + 
            "(Options: Education, Health/Wellness, Financial Empowerment, Environment, Social Services:  ")
            special_issue = input("What special issue does your org address?  ")
            self.create(org, contact, phone, email, web, primary_issue, special_issue)
        if command == "read":
            search = input("Would you like to search by organization name or primary social issue? Choose: org or issue  ")
            if org:
                org = input("Organization Name:  ")
            if issue:
                primary_issue = input("Primary Social Issue " + 
                "(Options: Education, Health/Wellness, Financial Empowerment, Environment, Social Services:  ")
            self.read(org, contact, phone, email, web, primary_issue, special_issue)
        if command == "update":
            update_org = input("What organization would you like to update?  ")
            if update_org != org:
                print("That organization is not in the database. Select 'create' to add it.")
            if update_org == org:
                org = input("Organization Name:  ")    
                contact = input("Contact Name:  ")
                phone = input("Contact Phone:  ")
                email = input("Contact Email:  ")
                web = input("Org Web Address:  ")
                primary_issue = input("What is your Primary Social Issue " + 
                "(Options: Education, Health/Wellness, Financial Empowerment, Environment, Social Services:  ")
                special_issue = input("What special issue does your org address?  ")
            self.update(org, contact, phone, email, web, primary_issue, special_issue)
        if command == "delete":
            org = input("Organization Name:  ")
            self.delete(org)

    def create(self, org, contact, phone, email, web, primary_issue, special_issue):
        # allow user to add to CP
        self.org = org
        self.contact = contact
        self.phone = phone
        self.email = email
        self.web = web
        self.primary_issue = primary_issue
        self.special_issue = special_issue

    def read(self, org, primary_issue):
        # allow user to look up a CP by org or issue
        # not sure how to call the rest of the values associated with this org or issue key
        self.org = org
        self.primary_issue = primary_issue

    def update(self, org, contact, phone, email, web, primary_issue, special_issue):
        # allow user to change info in CP
        # how do I make sure this updates instead of adding new?
        self.org = org
        self.contact = contact
        self.phone = phone
        self.email = email
        self.web = web
        self.primary_issue = primary_issue
        self.special_issue = special_issue

    def delete(self, org):
        # allow user to delete CP
        print("Do you want to delete {} from the community partner database? yes or no:  ".format(org)):
            if yes:
                del self.org
            else:
                return command()

    # after each command is executed, print stats of database
    # number of community partners in the database
    # number of orgs for each primary issue

if __name__ == "__main__":
    partner = CommunityPartner()
    partner.command()