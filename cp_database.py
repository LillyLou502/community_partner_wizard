

class CommunityPartner():
    def __init__(self, org, contact, phone, email, issue):
        self.org = org
        self.contact = contact
        self.phone = phone
        self.email = email
        self.issue = issue

database = [CommunityPartner("Metro United Way", "Jamie Miller", "502-550-5567", "jamie@muw.org", "Social Services"), 
            CommunityPartner("Boys and Girls Club", "Kathy Jones", "502-123-6789", "kathy@bgclub.org", "Education"),
            CommunityPartner("Earth and Spirit Center", "Bobby Hackett", "819-543-6543", "bobby@esc.org", "Environment"),
            CommunityPartner("Louisville Urban League", "Jennifer Michels", "502-345-0190", "jmichels@lul.org", "Social Services"),
            CommunityPartner("Norton Healthcare", "Bob Ross", "502-123-0009", "bob@norton.org", "Health/Wellness"),
            CommunityPartner("Nativity Academy", "Leslie Murphy", "502-345-5678", "leslie@nativity.org", "Education"),
            CommunityPartner("Metro Parks", "Tim Allen", "502-123-6789", "tallen@metrolou.org", "Environment"),
            CommunityPartner("Thrive Center", "Rosy Smith", "502-675-0987", "rsmith@thrive.org", "Health/Wellness")
]

issue_options = "Options: Education, Health/Wellness, Environment, Social Services"

def create(org, contact, phone, email, issue):
    database.append(CommunityPartner(org, contact, phone, email, issue))
    print("There are {} organizations in the Community Parnter Database.".format(len(database)))
    command()

def read_all():
    for item in database:
        print(item.org, item.contact, item.phone, item.email, item.issue, sep = ", ")
    command()

def read_by_issue(issue):
    match = 0
    for item in database:
        if item.issue == issue:
            match += 1
            print(item.org, item.contact, item.phone, item.email, item.issue, sep = ", ")
    if match == 0:
        print("There are no organizations with that social issue in the database.")
    command()

def read_by_org(org):
    for i, item in enumerate(database):
        if item.org == org:
            return i
    print("That organization is not in the database.")

def delete(org):
    org_index = read_by_org(org)
    if org_index == None:
        pass 
    else:
        database.pop(org_index)

def command():
    options = input("What do you want to do in the Community Partner Database? Choose: create, read, update, or delete. Type 'exit' to leave the program.   ")
    if options == "create":
        org = input("Organization Name:  ")
        contact = input("Contact Name:  ")
        phone = input("Contact Phone:  ")
        email = input("Contact Email:  ")
        issue = input("What is the Social Issue " + issue_options + ":  ")
        create(org, contact, phone, email, issue)
    if options == "read":
        read_choice = input("Do you want to read all entries or sort by or or issue? Type 'all' or 'issue':  ")
        if read_choice == "all":
            read_all()
        if read_choice == "issue":
            read_by_issue(input("What issue would you like to search? " + issue_options + ":  "))
    if options == "update":
        org = input("What organization information would you like to update?  ")
        delete(org)
        org = input("Organization Name:  ")    
        contact = input("Contact Name:  ")
        phone = input("Contact Phone:  ")
        email = input("Contact Email:  ")
        issue = input("What is the Social Issue " + issue_options + ":  ")
        create(org, contact, phone, email, issue)
    if options == "delete":
        org = input("What organization would you like to delete?  ")
        del_confirm = input("Do you want to delete {} from the community partner database? yes or no:  ".format(org))
        if del_confirm == "yes":
            delete(org)
            command()
        else:
            command()
    if options == "exit":
        pass

if __name__ == "__main__":
    command()
    print("There are {} organizations in the Community Parnter Database.".format(len(database)))