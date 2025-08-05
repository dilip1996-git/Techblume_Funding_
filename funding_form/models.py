from django.db import models


ROLE_CHOICES = [('student', 'Student'), ('sponsor', "Student's Sponsor")]
Employment_Choices = [('yes','Yes'),('no', 'No')]
Employment_select= [('permanant', 'Permanant'), ('goverment', 'Goverment'), ('fixed-term', 'Fixed-Term'), ('temporary', 'Temporary'),
                    ('independant consultant', 'Independant Consultant'), ('pensioner', 'Pensioner'),('selft-employed', 'Self-EMployed')]
course_duration= [('1 Month', '1 MOnth'), ('2 months','2 Months'), ('3 months', '3 Months'), ('5 months', '5 Months'),
                  ('6 months', '6 Months'), ('8 months', '8 Months'), ('9 months', '9 Months'), ('1 year', '1Year'),
                  ('2 years', '2 Years'), ('3 years', '3 Years'), ('4 years', '4 Years'), ('5 years', '5 Years')]
courses = [('diploma in Full stack Development', 'Diploma in Full-Stack development'),
           ('diploma in Data Science', 'Diploma in Data Science'),
           ('cyber security', 'Diploma in Cyber Security'), ('ui/ux design', 'Diploma in UI/UX Design')]
Id_type= [('south african identity number', 'South African Identity Number'),
          ('passport or permit number', 'Passport or Permit Number')]
Gender = [('male', 'Male'), ('female', 'Female')]
provinace = [('gauteng', 'Gauteng'), ('western cape', 'Western Cape'), ('kwazulu-natl', 'KwaZulu-Natal'), ('eastern cape', 'Eastern Cape'),
             ('free state', 'Free State'), ('limpopo', 'Limpopo'), ('mpumalanga', 'Mpumalanga'),
             ('northen cape', ' Northen Cape'), ('north west', 'North West')]


class Application(models.Model):
    CRM_ID = models.CharField(max_length=50, blank=True, null=True)
    Select_your_role =  models.CharField(max_length=100, choices=ROLE_CHOICES)
    Are_you_currently_employed = models.CharField(max_length=100,choices=Employment_Choices )
    Select_your_Employment_Status = models.CharField(max_length=100, choices=Employment_select)
    Gross_income= models.IntegerField()
    Net_Income = models.IntegerField()
    Additional_Income = models.IntegerField()
    Tuition_fee_to_be_funded = models.IntegerField()
    Course_Name = models.CharField(max_length=100, choices= courses)
    Select_the_total_course_duration = models.CharField(max_length=100, choices=course_duration) 
    Your_Name = models.CharField(max_length=50)
    Your_Surname = models.CharField(max_length=50)
    Your_ID_type = models.CharField(max_length=150, choices=Id_type)
    Your_ID_Number = models.BigIntegerField()
    Your_Primary_Contact_Number = models.BigIntegerField
    Your_Alternate_contact_number = models.BigIntegerField()
    Your_Parent_Contact_number = models.BigIntegerField()
    Your_Email_Address = models.EmailField()
    Your_Gender = models.CharField(max_length=100, choices=Gender)
    Your_Province = models.CharField(max_length=100, choices= provinace)
    Your_Address_with_Zip_Code = models.CharField(max_length=250)


