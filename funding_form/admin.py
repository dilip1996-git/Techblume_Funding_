from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'Your_Name', 'Your_Surname', 'Course_Name', 'Select_the_total_course_duration',
        'Select_your_role', 'Are_you_currently_employed', 'Select_your_Employment_Status',
        'Tuition_fee_to_be_funded', 'Your_Email_Address', 'Your_Primary_Contact_Number', 'CRM_ID'
    )

    search_fields = (
        'Your_Name', 'Your_Surname', 'Your_Email_Address',
        'Your_ID_Number', 'Your_Primary_Contact_Number', 'CRM_ID'
    )

    list_filter = (
        'Select_your_role', 'Select_your_Employment_Status',
        'Course_Name', 'Select_the_total_course_duration', 'Your_Province', 'Your_Gender'
    )

    # CRM_ID is now editable, so no need to make it read-only
