# get the CP database
# import re - do I need this?
# import os

class CommunityPartner():
    # create a dictionary inside the class
    def __init__(self, org, contact, phone, email, issue):
        self.org = org
        self.contact = contact
        self.phone = phone
        self.email = email
        self.issue = issue

    @property
    def CP_dict(self):
        return {"Organization": self.org,
                "Contact Name": self.contact,
                "Phone Number": self.phone,
                "Email Address": self.email,
                "Social Issue": self.issue}

database = [CommunityPartner("Metro United Way", "Theresa Reno-Weber", "502-550-5567", "theresa@muw.org", "Social Services"), 
            CommunityPartner("Boys and Girls Club", "Kathy Jones", "502-123-6789", "kathy@bgclub.org", "Education"),
            CommunityPartner("Earth and Spirit Center", "Bobby Hackett", "819-543-6543", "bobby@esc.org", "Environment"),
            CommunityPartner("Louisville Urban League", "Sadiqa Reynolds", "502-345-0190", "sadiqa@lul.org", "Social Services"),
            CommunityPartner("Norton Healthcare", "Bob Ross", "502-123-0009", "bob@norton.org", "Health/Wellness"),
            CommunityPartner("Nativity Academy", "Ebony O'Rea", "502-345-5678", "ebony@nativity.org", "Education"),
            CommunityPartner("Metro Parks", "Tim Allen", "502-123-6789", "tallen@metrolou.org", "Environment"),
            CommunityPartner("Thrive Center", "Rosy Smith", "502-675-0987", "rsmith@thrive.org", "Health/Wellness")
]

issue_options = "Options: Education, Health/Wellness, Environment, Social Services"

def create(org, contact, phone, email, issue):
    database.append(CommunityPartner(org, contact, phone, email, issue))
    print("There are {} organizations in the Community Parnter Database.".format(len(database)))
    command()

def read_all():
    print(*database, sep = "\n")
    # for item in range(len(database)):
    #     print(database[item]) # This is not printing the actual names...just the location of the partners.
    #     command()
    # print(database)
    # for item in database:
        # print(CommunityPartner(org, contact, phone, email, issue))
        # print(item) # This is not running through all of the items and printing them.

def read_by_issue(issue):
    for item in database:
        if item.issue == issue:
            print(item.issue) # this prints the location of the org but not the org dictionary/class. i want to print all orgs associated with this issue.
            command()
            # print(CommunityPartner(org, contact, phone, email, issue)) # this doesn't work either

def read_by_org(org):
    for i, item in zip(database):
        if item.org == org:
            return i
            command()
        elif i == None:
            print("That organization is not in the database.") # this is not happening.
            command()

def delete(org):
    org_index = read_by_org(org)
    if org_index:
        database.pop(org_index)
    else:
        print("That organization is not in the database.")
        command()

def command():
    command = input("What do you want to do in the Community Partner Database? Choose: create, read, update, or delete. Type 'exit' to leave the program.   ")
    if command == "create":
        org = input("Organization Name:  ")
        contact = input("Contact Name:  ")
        phone = input("Contact Phone:  ")
        email = input("Contact Email:  ")
        issue = input("What is the Social Issue " + issue_options + ":  ")
        create(org, contact, phone, email, issue)
    if command == "read":
        read_choice = input("Do you want to read all entries or sort by or or issue? Type 'all' or 'org' or 'issue':  ")
        if read_choice == "all":
            read_all()
        if read_choice == "org":
            read_by_org(input("What organization would you like to search?  "))
        if read_choice == "issue":
            read_by_issue(input("What issue would you like to search? " + issue_options + ":  "))
    if command == "update":
        org = input("What organization information would you like to update?  ")
        delete(org)
        org = input("Organization Name:  ")    
        contact = input("Contact Name:  ")
        phone = input("Contact Phone:  ")
        email = input("Contact Email:  ")
        issue = input("What is the Social Issue " + issue_options + ":  ")
        create(org, contact, phone, email, issue)
    if command == "delete":
        org = input("What organization would you like to delete?  ")
        print("Do you want to delete {} from the community partner database? yes or no:  ".format(org))
        if "yes":
            delete(org)
        else:
            command()
    if command == "exit":
        pass

if __name__ == "__main__":
    command()
    print("There are {} organizations in the Community Parnter Database.".format(len(database)))
# After someone does one action in the CPDatabase, I want to ask them if they are done. If they want to do more, circle back to command. If they are done, type exit.

    # print("Education Organizations = {} \n".format(len(database(issue == "Education"))) + 
    #     "Health/Wellness Organizations = {} \n".format(len.database(issue == "Health/Wellness")) +
    #     "Environment Organizations = {} \n".format(len.database(issue == "Environment")) +
    #     "Social Service Organizations = {} \n".format(len.database(issue == "Social Services")))
    # after each command is executed, print stats of database
    # number of community partners in the database
    # number of orgs for each primary issue


# def command():
#     command = input("What do you want to do in the Community Partner Database? Choose: create, read, update, or delete:   ")
#     if command == "create":
#         org = input("Organization Name:  ")
#         contact = input("Contact Name:  ")
#         phone = input("Contact Phone:  ")
#         email = input("Contact Email:  ")
#         primary_issue = input("What is your Primary Social Issue " + 
#         "(Options: Education, Health/Wellness, Environment, Social Services:  ")
#         create(org, contact, phone, email, primary_issue)
#     if command == "read":
#         search = input("Would you like to search by organization name or primary social issue? Choose: org or issue  ")
#         if search == "org":
#             org = input("Organization Name:  ")
#             return CP_dict
#         if search = "issue":
#             primary_issue = input("Primary Social Issue " + 
#             "(Options: Education, Health/Wellness, Environment, Social Services:  ")
#             return CP_dict({}.format(primary_issue)) # need this to be sorted by issue and return all records with the selected issue
#         self.read(org, contact, phone, email, primary_issue)
#     if command == "update":
#         update_org = input("What organization information would you like to update?  ")
#         CP_dict.get("Organization": update_org)
#         return CP_dict(org, contact, phone, email, primary_issue, special_issue)
#             org = input("Organization Name:  ")    
#             contact = input("Contact Name:  ")
#             phone = input("Contact Phone:  ")
#             email = input("Contact Email:  ")
#             primary_issue = input("What is your Primary Social Issue " + 
#             "(Options: Education, Health/Wellness, Environment, Social Services:  ")
#         if update_org == org: # not sure how to find an org name
            
#         if update_org != org:
#             print("That organization is not in the database. Select 'create' to add it.")
#             return command()
#         self.update(org, contact, phone, email, primary_issue)
#     if command == "delete":
#         org = input("Organization Name:  ")
#         print("Do you want to delete {} from the community partner database? yes or no:  ".format(org)):
#         if yes:
#             del self.org
#         else:
#             return command()
#         self.delete(org)

    # def create(self, org, contact, phone, email, web, primary_issue):
    #     # allow user to add to CP
    #     self.org = org
    #     self.contact = contact
    #     self.phone = phone
    #     self.email = email
    #     self.web = web
    #     self.primary_issue = primary_issue

    # def read(self, org, primary_issue):
    #     # allow user to look up a CP by org or issue
    #     # not sure how to call the rest of the values associated with this org or issue key
    #     self.org = org
    #     self.primary_issue = primary_issue

    # def update(self, org, contact, phone, email, web, primary_issue):
    #     # allow user to change info in CP
    #     # how do I make sure this updates instead of adding new?
    #     self.org = org
    #     self.contact = contact
    #     self.phone = phone
    #     self.email = email
    #     self.web = web
    #     self.primary_issue = primary_issue

    # def delete(self, org):
    #     # allow user to delete CP
    #     print("Do you want to delete {} from the community partner database? yes or no:  ".format(org)):
    #         if yes:
    #             del self.org
    #         else:
    #             return command()

    # after each command is executed, print stats of database
    # number of community partners in the database
    # number of orgs for each primary issue

