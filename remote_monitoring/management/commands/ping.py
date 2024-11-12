
from datetime import timedelta, timezone
import time
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from remote_monitoring.models import Machine, Email
from django.utils import timezone
from django.conf import settings

class Command(BaseCommand):
    help = 'Run a scheduled task'

    def handle(self, *args, **kwargs):

        try:
         while True:
            current_time = timezone.now()
            machines = Machine.objects.all()
            

            for machine in machines:
                  time_diff = current_time - machine.timestamp
                  if time_diff > timedelta(minutes=3):
                    # emails = Email.objects.filter(machine_id=machine.id)
                    # for email in emails:
                    #  send_mail(
                    #        subject=f'Machine {machine.id} is not responding',
                    #        message=f'The machine with ID {machine.id} has not sent a ping in over 2 minutes.',
                    #        from_email=settings.EMAIL_HOST_USER,
                    #        recipient_list=[email.primary_email, email.secondary_email, email.optional1_email, email.optional2_email, email.optional3_email],
                    #        fail_silently=False,
                    #      )
                     print(f"Email sent to {machine.id} for machine {machine.id}")

                     machine.status = 'unhealthy'
                     machine.save()
                  else:
                      print(f"Machine {machine.id} is healthy")
                      machine.status = 'healthy'
                      machine.save()
           
            
            # Wait for 20 seconds before running the task again
            time.sleep(20)

        except KeyboardInterrupt:
           self.stdout.write(self.style.WARNING('Command interrupted! Exiting...'))
        except Exception as e:
           self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))   

