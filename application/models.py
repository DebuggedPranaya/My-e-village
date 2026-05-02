from django.db import models

# Create your models here.
from django.db import models

class enquiryform(models.Model):

    SUBJECT_CHOICES = [
        ('general', 'General inquiry'),
        ('scholarship', 'Scholarship'),
        ('agriculture', 'Agriculture'),
        ('infrastructure', 'Infrastructure'),
        ('complaint', 'Complaint'),
    ]

    name        = models.CharField(max_length=100)
    phone       = models.CharField(max_length=15)
    subject     = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message     = models.TextField(blank=True)

    
    def __str__(self):
        return self.name
    


class Announcement(models.Model):

    CATEGORY_CHOICES = [
        ('notice', 'Notice'),
        ('scheme', 'Scheme'),
        ('agri', 'Agriculture'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    expiry_date = models.DateField(null=True, blank=True)
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Festival(models.Model):
    MONTH_CHOICES = [
        ('jan_feb', 'January / February'),
        ('feb_mar', 'February / March'),
        ('mar_apr', 'March / April'),
        ('apr_may', 'April / May'),
        ('may_jun', 'May / June'),
        ('jun_jul', 'June / July'),
        ('jul_aug', 'July / August'),
        ('aug_sep', 'August / September'),
        ('sep_oct', 'September / October'),
        ('oct_nov', 'October / November'),
        ('nov_dec', 'November / December'),
        ('dec_jan', 'December / January'),
    ]

    name        = models.CharField(max_length=100)
    month       = models.CharField(max_length=20, choices=MONTH_CHOICES)
    description = models.TextField()
    image       = models.ImageField(upload_to='festivals/')
    order       = models.PositiveIntegerField(default=0)  # controls display order

    def __str__(self):
        return self.name

   
