from django.db import models

# Machines Table
class Machine(models.Model):
    machine_name = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,null=False,blank=False, default='unhealthy')


    def __str__(self):
        return self.machine_name

# Emails Table
class Email(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='emails')
    primary_email = models.EmailField(null=False, blank=False, max_length=100)
    secondary_email = models.EmailField(null=False, blank=False, max_length=100)
    optional1_email = models.EmailField(max_length=100)
    optional2_email = models.EmailField(max_length=100)
    optional3_email = models.EmailField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['machine']),
            models.Index(fields=['primary_email','secondary_email','optional1_email','optional2_email','optional3_email'])
           
        ]

    def __str__(self):
        return self.machine.machine_name
    


#Session_status_table
class Session(models.Model):
    session_status = models.CharField(max_length=50)
    def __str__(self):
        return self.session_status    
      

 #survey table
class Survey(models.Model):

    question_1_response = models.BooleanField(null=True, blank=False, default='N/A') # Response for the first static question
    question_2_response = models.BooleanField(null=True, blank=False,default='N/A')  # Response for the second static question
   

    class Meta:
        indexes = [

            models.Index(fields=['question_1_response','question_2_response'])
           
        ]   

    def __str__(self):
        return f"Survey {self.id}: Q1 - {self.question_1_response}, Q2 - {self.question_2_response}"
    

# Metrics Table
class UserMetrics(models.Model):
 machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine', default=1)
 session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='session', default=12)
 survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey', default=1)
 time_engaged = models.IntegerField(null=False, blank=False)
 distance_while_active = models.IntegerField(null=False, blank=False)
 hand_position = models.IntegerField(null=False, blank=False)
 rate= models.IntegerField(null=False, blank=False)
 compression = models.IntegerField(null=False, blank=False)
 recoil = models.IntegerField(null=False, blank=False)
 watched_animation = models.BooleanField(null=False, blank=False)
 sessions_played = models.IntegerField(null=False, blank=False)

 class Meta:
        indexes = [
            models.Index(fields=['session','machine','survey'])   
           
        ] 

 def __str__(self):
        return self.machine.machine_name    
 

 





