from django.shortcuts import render, redirect,get_object_or_404
from django.forms import inlineformset_factory
from .models import Resume, Education, Experience, Skill,Project,Certification
from .forms import ResumeForm, EducationForm, ExperienceForm, SkillForm,ProjectForm,CertificationForm
from django.http import JsonResponse
from django.urls import reverse
from collections import defaultdict
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse, Http404
import io

def create_resume(request):
    EducationFormSet = inlineformset_factory(Resume, Education, form=EducationForm, extra=1)
    ExperienceFormSet = inlineformset_factory(Resume, Experience, form=ExperienceForm, extra=1)
    SkillFormSet = inlineformset_factory(Resume, Skill, form=SkillForm, extra=1)
    ProjectFormSet = inlineformset_factory(Resume, Project, form=ProjectForm, extra=1)
    CertificationFormSet = inlineformset_factory(Resume, Certification, form=CertificationForm, extra=1)
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST)
        education_formset = EducationFormSet(request.POST,prefix='education')
        experience_formset = ExperienceFormSet(request.POST,prefix='experience')
        skill_formset = SkillFormSet(request.POST,prefix='skill')
        project_formset = ProjectFormSet(request.POST,prefix='project')
        certification_formset = CertificationFormSet(request.POST,prefix='certification')
        if (
            resume_form.is_valid() and
            education_formset.is_valid() and
            experience_formset.is_valid() and
            skill_formset.is_valid() and
            project_formset.is_valid() and
            certification_formset.is_valid()
        ):
            resume = resume_form.save(commit=False)
            if request.user.is_authenticated:
                resume.user = request.user
            resume.save()
            education_formset.instance = resume
            experience_formset.instance = resume
            skill_formset.instance = resume
            project_formset.instance = resume
            certification_formset.instance = resume
            education_formset.save()
            experience_formset.save()
            skill_formset.save()
            project_formset.save()
            certification_formset.save()
            return JsonResponse({
                'status': 'success',
                'redirect_url': reverse('preview_resume', args=[resume.slug])
            })
        else:
            all_errors = {}
            for field, errors in resume_form.errors.items():
                all_errors[field] = list(errors)
            for i, form in enumerate(education_formset.forms):
                for field, errors in form.errors.items():
                    all_errors[f'education-{i}-{field}'] = list(errors)
            for i, form in enumerate(experience_formset.forms):
                for field, errors in form.errors.items():
                    all_errors[f'experience-{i}-{field}'] = list(errors)
            for i, form in enumerate(skill_formset.forms):
                for field, errors in form.errors.items():
                    all_errors[f'skill-{i}-{field}'] = list(errors)
            for i, form in enumerate(project_formset.forms):
                for field, errors in form.errors.items():
                    all_errors[f'project-{i}-{field}'] = list(errors)
            for i, form in enumerate(certification_formset.forms):
                for field, errors in form.errors.items():
                    all_errors[f'certification-{i}-{field}'] = list(errors)
            return JsonResponse({
                'status': 'error',
                'errors': all_errors
            }, status=400)
    else:
        resume_form = ResumeForm()
        education_formset = EducationFormSet(prefix='education')
        experience_formset = ExperienceFormSet(prefix='experience')
        skill_formset = SkillFormSet(prefix='skill')
        project_formset = ProjectFormSet(prefix='project')
        certification_formset = CertificationFormSet(prefix='certification')
    return render(request, 'resume/create.html', {
        'resume_form': resume_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
        'certification_formset': certification_formset,
    })
        
def preview_resume(request, slug):
    try:
        resume = Resume.objects.get(slug=slug)
        skills_grouped = defaultdict(list)
        for skill in resume.skills.all():
            skills_grouped[skill.category].append(skill.name)
        return render(request, 'resume/preview.html', {
            'resume': resume,
            'skills_grouped': dict(skills_grouped)
        })
    except Resume.DoesNotExist:
        raise Http404("Resume not found")

def dashboard(request):
    resumes = Resume.objects.all().order_by('id')
    return render(request,'resume/dashboard.html',{'resumes':resumes})

def edit_resume(request, slug):
    resume = get_object_or_404(Resume, slug=slug)
    EducationFormSet = inlineformset_factory(Resume, Education, form=EducationForm, extra=0, can_delete=True)
    ExperienceFormSet = inlineformset_factory(Resume, Experience, form=ExperienceForm, extra=0, can_delete=True)
    SkillFormSet = inlineformset_factory(Resume, Skill, form=SkillForm, extra=0, can_delete=True)
    ProjectFormSet = inlineformset_factory(Resume, Project, form=ProjectForm, extra=0, can_delete=True)
    CertificationFormSet = inlineformset_factory(Resume, Certification, form=CertificationForm, extra=0, can_delete=True)
    if request.method == 'POST':
        resume_form = ResumeForm(request.POST, instance=resume)
        education_formset = EducationFormSet(request.POST, instance=resume, prefix='education')
        experience_formset = ExperienceFormSet(request.POST, instance=resume, prefix='experience')
        skill_formset = SkillFormSet(request.POST, instance=resume, prefix='skill')
        project_formset = ProjectFormSet(request.POST, instance=resume, prefix='project')
        certification_formset = CertificationFormSet(request.POST, instance=resume, prefix='certification')
        if (
            resume_form.is_valid() and
            education_formset.is_valid() and
            experience_formset.is_valid() and
            skill_formset.is_valid() and
            project_formset.is_valid() and
            certification_formset.is_valid()
        ):
            resume_form.save()
            education_formset.save()
            experience_formset.save()
            skill_formset.save()
            project_formset.save()
            certification_formset.save()
            return JsonResponse({
                'status': 'success',
                'redirect_url': reverse('preview_resume', args=[resume.slug])
            })
    else:
        resume_form = ResumeForm(instance=resume)
        education_formset = EducationFormSet(instance=resume, prefix='education')
        experience_formset = ExperienceFormSet(instance=resume, prefix='experience')
        skill_formset = SkillFormSet(instance=resume, prefix='skill')
        project_formset = ProjectFormSet(instance=resume, prefix='project')
        certification_formset = CertificationFormSet(instance=resume, prefix='certification')
    return render(request, 'resume/create.html', {
        'resume_form': resume_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
        'certification_formset': certification_formset,
        'is_edit': True
    })

def download_pdf(request, slug):
    user_profile = get_object_or_404(Resume, slug=slug)
    skills_grouped = defaultdict(list)
    for skill in user_profile.skills.all():
        skills_grouped[skill.category].append(skill.name)
    template_path = 'resume/download.html'
    context = {'resume': user_profile,'skills_grouped': dict(skills_grouped)}
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={user_profile.name}_CV.pdf'
    pisa_status = pisa.CreatePDF(
        io.BytesIO(html.encode('UTF-8')),
        dest=response,
        encoding='UTF-8'
    )
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
