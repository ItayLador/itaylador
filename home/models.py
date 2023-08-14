from django.db import models

# Create your models here.


CATAGORIES = [
   ( "Get Curious", "Get Curious",),
   ( "Getting Started", "Getting Started",),
   ( "Developing Your Idea", "Developing Your Idea",),
   ( "Accelerate Your Venture", "Accelerate Your Venture",),
   ( "Competitions", "Competitions",),
   ( "Speaker Series", "Speaker Series",),
   ( "Student Clubs", "Student Clubs",),
]

class stats(models.Model):
    num = models.CharField(max_length=100)
    des = models.CharField(max_length=200)

class catagory(models.Model):
    catagory = models.CharField(max_length=250, primary_key=True)
    text = models.TextField(blank=True)

class course(models.Model):
    course = models.TextField(primary_key=True)
    offeredIn = models.CharField(max_length=220)
    description = models.TextField()
    catagories = models.ManyToManyField(catagory, blank=True, related_name="+")
    requiredForMinor = models.BooleanField(default=False)
    capstone = models.BooleanField(default=False)

class skill(models.Model):
    skill = models.TextField(primary_key=True)

class coursePage(models.Model):
    kind = models.CharField(max_length=120, primary_key=True)
    courses = models.ManyToManyField(course, related_name="+", blank=True)
    moto = models.TextField(blank=True)
    skills = models.ManyToManyField(skill, related_name="+", blank=True)
    intro = models.TextField(blank=True)
    description = models.TextField(blank=True)
    extra = models.TextField(blank=True)

class events(models.Model):
    event = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    location = models.TextField()
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    image = models.FileField(upload_to="img/")
    catagories = models.ManyToManyField(catagory, related_name="+")

class alumni(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    buisness = models.CharField(max_length=250)
    picture = models.FileField(upload_to="img/")
    buisnessPicture = models.FileField(upload_to="img/")
    buisnessDescription = models.TextField()
    value = models.CharField(default="0", max_length=250)

class member(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    picture = models.FileField(upload_to="img/")
    position = models.CharField(max_length=250)
    schedule = models.TextField(max_length=250)
    description = models.TextField(blank=True)
    isFaculty = models.BooleanField(default=False)
    email = models.TextField(blank=True)

class requirement(models.Model):
    requirement = models.TextField()

class expect(models.Model):
    expect = models.TextField(primary_key=True)

class clubs(models.Model):
    club = models.CharField(max_length=125, primary_key=True)
    description = models.TextField()
    link = models.TextField()

class date(models.Model):
    date = models.DateField()
    description = models.TextField(blank=True)

class developingProgram(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    description = models.TextField()
    preview = models.TextField(blank=True)
    requirements = models.ManyToManyField(requirement, related_name="+")
    dates = models.ManyToManyField(date, related_name="+", blank=True)  
    application = models.TextField(blank=True) 
    
    def hasTimeline(self):
        if len(self.dates.all()) > 0:
            return True
        else:
             return False
    
    def hasApplication(self):
        if len(self.application) > 0:
            return True
        else:
            return False

    
class schedule(models.Model):
    day = models.IntegerField(default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField()

class curiousProgram(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    description = models.TextField()
    openFor = models.CharField(max_length=250)
    year = models.IntegerField()
    hasSchedule = models.BooleanField(default=False)
    schedules = models.ManyToManyField(schedule, related_name="+", blank=True)
    preview = models.TextField(blank=True)

class startProgram(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    description = models.TextField(blank=True)
    who = models.TextField(blank=True)
    when = models.TextField(blank=True)

class activity(models.Model):
    activity = models.TextField()

class ventureProgram(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    preview = models.TextField(blank=True)
    description = models.TextField(blank=True)
    hasRecieving = models.BooleanField(default=True)
    recievingSupervisor = models.ManyToManyField(expect, related_name="s+", blank=True)
    recievingStudent = models.ManyToManyField(expect, related_name="st+", blank=True)
    who = models.TextField()
    activities = models.ManyToManyField(activity, blank=True, related_name="+")
    application = models.TextField(blank=True)

class rounds(models.Model):
    name = models.CharField(max_length=250)
    hasDescription = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    description = models.TextField(blank=True)


class prize(models.Model):
    prize = models.TextField(primary_key=True)
    who = models.TextField(blank=True)

class competition(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    description = models.TextField(blank=True)
    preview = models.TextField(blank=True)
    requirements = models.ManyToManyField(requirement, related_name="+")
    hasPrize = models.BooleanField(default=False)
    prizes = models.ManyToManyField(prize, blank=True, related_name="+")
    application = models.TextField(blank=True)
    rounds = models.ManyToManyField(rounds, blank=True, related_name="+")
    def hasRounds(self):
        if len(self.rounds.all()) > 0:
            return True
        else:
            return False

class about(models.Model):
    image = models.FileField(upload_to="img/")
    text = models.TextField()  

class previousSpeaker(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    tite = models.TextField(blank=True)
    image = models.FileField(upload_to="img/")
    orgImg = models.FileField(upload_to="img/", blank=True)

class launch(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="img/")

class NotionLink(models.Model):
    link = models.TextField(primary_key=True)


class FairParticipant(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    industry = models.TextField()
    description = models.TextField()
    hiring = models.TextField()
    image = models.FileField(upload_to="img/")
    link = models.TextField(blank=True)

class FairYear(models.Model):
    year = models.IntegerField(primary_key=True)
    members = models.ManyToManyField(FairParticipant, blank=True, related_name="+")

class JobFair(models.Model):
    program = models.CharField(max_length=250, primary_key=True)
    image = models.FileField(upload_to="img/")
    description = models.TextField(blank=True)
    who = models.TextField(blank=True)
    preview = models.TextField(blank=True)
    years = models.ManyToManyField(FairYear, blank=True, related_name="+")











