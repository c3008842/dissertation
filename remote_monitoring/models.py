from django.db import models

# Machines Table
class Machine(models.Model):
    machine_name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

# Emails Table
class Email(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='emails')
    primary_email = models.EmailField(null=False, blank=False)
    secondary_email = models.EmailField(null=False, blank=False)
    optional1_email = models.EmailField()
    optional2_email = models.EmailField()
    optional3_email = models.EmailField()


    def __str__(self):
        return self.email_address





