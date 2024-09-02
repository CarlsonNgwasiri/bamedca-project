from django.db import models

# Model for general "About Us" information on your site
class AboutModel(models.Model):
    # Title of the About section
    title = models.CharField(max_length=50)
    # Description providing detailed information about the organization
    description = models.TextField(max_length=1000)
    # Name of the organization or entity
    name = models.CharField(max_length=50)
    # Names of the members
    members = models.CharField(max_length=50)
    # The active town or location of the organization
    activeTown = models.CharField(max_length=50)
    # Image representing the About section
    image = models.ImageField(upload_to='about')
    # more details
    paragraph1 = models.TextField(max_length=1000)
    # more details
    paragraph2 = models.TextField(max_length=1000)
    # more details
    paragraph3 = models.TextField(max_length=1000)
    # Executive committee members' roles
    excoPresi = models.CharField(max_length=50, default='')
    excoVP = models.CharField(max_length=50, default='')
    excoSG = models.CharField(max_length=50, default='')
    # Introduction texts for executives
    introPresi = models.CharField(max_length=200, default='')
    introVP = models.CharField(max_length=200, default='')
    introSG = models.CharField(max_length=200, default='')
    # Images of the executives
    presiImage = models.ImageField(upload_to='about', default='')
    vpImage = models.ImageField(upload_to='about', default='')
    sgImage = models.ImageField(upload_to='about', default='')

    def __str__(self):
        return self.name

# Model for branch information
class BranchModel(models.Model):
    # Title of the branch
    title = models.CharField(max_length=50)
    # Description providing details about the branch
    description = models.TextField(max_length=1000)
    # Town where the branch is located
    town = models.CharField(max_length=50)
    # Additional description about the branch
    subDescription = models.CharField(max_length=100, default='')
    # Names and roles related to the branch
    president = models.CharField(max_length=50)
    fonRep = models.CharField(max_length=50)
    # Quarters associated with this branch
    quater = models.CharField(max_length=50)
    # Venue for meetings
    meetingVenue = models.CharField(max_length=50)
    # Members associated with the branch
    members = models.CharField(max_length=50)
    # Image representing the branch
    image = models.ImageField(upload_to='branch')
    # Executive committee members' roles
    excoPresi = models.CharField(max_length=50, default='')
    excoVP = models.CharField(max_length=50, default='')
    excoSG = models.CharField(max_length=50, default='')
    # Introduction texts for executives
    introPresi = models.CharField(max_length=200, default='')
    introVP = models.CharField(max_length=200, default='')
    introSG = models.CharField(max_length=200, default='')
    # Images of the executives
    presiImage = models.ImageField(upload_to='branch', default='')
    vpImage = models.ImageField(upload_to='branch', default='')
    sgImage = models.ImageField(upload_to='branch', default='')

    def __str__(self):
        return self.town

# Model for events
class EventModel(models.Model):
    # Title of the event
    title = models.CharField(max_length=100)
    # Description providing details about the event
    description = models.TextField(max_length=1000)
    # Period or date range for the event
    period = models.CharField(max_length=100)
    # more details about the event
    paragraph1 = models.TextField(max_length=1000)
    # more details about the event
    paragraph2 = models.TextField(max_length=1000)
    # more details about the event
    paragraph3 = models.TextField(max_length=1000)
    # more details about the event
    image = models.ImageField(upload_to='events')

    def __str__(self):
        return self.title

# Model for projects
class ProjectModel(models.Model):
    # Title of the project
    title = models.CharField(max_length=100)
    # Description providing details about the project
    description = models.TextField(max_length=1000)
    # more details about the project
    paragraph1 = models.TextField(max_length=1000)
    # more details about the project
    paragraph2 = models.TextField(max_length=1000)
    # more details about the project
    paragraph3 = models.TextField(max_length=1000)
    # more details about the event
    # Image representing the project
    image = models.ImageField(upload_to='projects')
    
    def __str__(self):
        return self.title

# Model for executive committee members
class ExecutiveModel(models.Model):
    # Name of the executive
    name = models.CharField(max_length=50)
    # Role of the executive
    role = models.CharField(max_length=50)
    # Introduction or bio of the executive
    intro = models.TextField(max_length=100)
    # Image of the executive
    image = models.ImageField(upload_to='about', default='')
    
    def __str__(self):
        return self.name

# Model for contact information related to quarters
class ContactModel(models.Model):
    # Quarter or division for which the contact information is relevant
    quater = models.CharField(max_length=100, default='')
    # Phone number for contact
    phone = models.CharField(max_length=100, default='')
    # Email address for contact
    email = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.quater

# Model for quarters associated with a branch
class QuaterModel(models.Model):
    # Foreign key linking each quarter to a specific branch
    branch = models.ForeignKey(BranchModel, related_name='quarters', on_delete=models.CASCADE)
    # Name of the quarter
    name = models.CharField(max_length=100, default='')
    # Head or leader of the quarter
    head = models.CharField(max_length=100, default='')
    # Contact information for the quarter
    contact = models.CharField(max_length=100, default='')
    # Meeting location for the quarter
    meeting_location = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='quarter', default='')

    def __str__(self):
        return self.name
