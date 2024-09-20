from django.db import models

# Create your models here.
# decalre a new model with a name "myapp"
class thing(models.Model):
    #model Field
    title = models.CharField(max_length=100)
    description = models.TextField()
    #rename obejct of model with it title name
    def __str__(self):
        return self.title
        #return self.description
        #def __str__(self):
        #return f"{self.name} - {self.description}"