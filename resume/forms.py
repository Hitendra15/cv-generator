from django import forms
from .models import Resume,Education,Experience,Skill,Certification,Project

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title','name','email','phone','summary','linkedin','github']
        labels = {
            'name': 'Full Name',
            'title': 'Professional Title',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'summary': 'Professional Summary',
            'linkedin': 'LinkedIn URL',
            'github': 'GitHub URL',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. John Doe'
            }),
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Software Engineer'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. john.doe@example.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. 9876543210'
            }),
            'summary': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Write a short professional summary about yourself, your experience, and key skills...'
            }),
            'linkedin': forms.URLInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. https://linkedin.com/in/yourname'
            }),
            'github': forms.URLInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. https://github.com/yourname'
            }),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('resume',)
        labels = {
            'degree': 'Degree',
            'institution': 'Institution',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'field_of_study': 'Field of Study',
            'grade': 'Grade / GPA',   
            'location': 'Location',
        }
        widgets = {
            'degree': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. B.Tech in Computer Science'
            }),
            'institution': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. IIT Bombay'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
            'field_of_study': forms.TextInput(attrs={'class':'input',
                'placeholder': 'e.g. Computer Science, Mechanical Engineering'
            }),
            'grade': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. 9.57 or First Class'
            }),
            'location': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Mumbai, India'
            }),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ('resume',)
        labels = {
            'job_title': 'Job Title',
            'company': 'Company Name',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'description': 'Responsibilities',
            'location': 'Location',
        }
        widgets = {
            'job_title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Backend Developer'
            }),
            'company': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Infosys'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Describe your role, achievements, and technologies used...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Mumbai, India'
            }),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ('resume',)
        labels = {
            'name': 'Skill',
            'level': 'Level',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Python, Django, React'
            }),
            'level': forms.Select(attrs={'class':'dropdown'})
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('resume',)
        labels = {
            'title': 'Project Title',
            'description': 'Project Description',
            'link': 'Project Links',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. E-commerce Website'
            }),
            'description': forms.Textarea(attrs={
                'class': 'textarea',
                'placeholder': 'Explain what the project does, technologies used, and your role...'
            }),
            'link': forms.TextInput(attrs={'class':'input',
            'placeholder': 'e.g. https://github.com/your-project or live demo URL'})
        }
        error_messages = {
            'link':{'invalid': 'Enter a valid URL (e.g. https://example.com)'}
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        exclude = ('resume',)
        labels = {
            'name': 'Certification Name',
            'organization': 'Issuing Organization',
            'date': 'Completion Date',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. AWS Certified Developer'
            }),
            'organization': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'e.g. Amazon Web Services'
            }),
            'date': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),
        }