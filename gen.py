baseURL = "https://hkpeterpeter.github.io"
#baseURL = "http://127.0.0.1:8080"

from jinja2 import Environment, FileSystemLoader
from data.navbar import navbar_text, navbar_icon, navbar_menu
from data.social import social
from data.slideshow import slideshow
from data.profile import author, email, job_title, office_room, office_sub, office_url, keywords, homepage_text, profile_description, profile_roles, profile_url
from data.academic import academic_title, academic, academic_length
from data.educator import educator_title, educator, educator_length
from data.teaching_awards import teaching_awards_title, teaching_awards, teaching_awards_length
from data.hackathon_roles import hackathon_roles_title, hackathon_roles, hackathon_roles_length
from data.hackathon_awards import hackathon_awards_title, hackathon_awards, hackathon_awards_length
from data.volunteer_roles import volunteer_roles_title, volunteer_roles, volunteer_roles_length
from data.cyberport_alum import cyberport_alum_title, cyberport_alum_roles
from data.cse_alum import cse_alum_title, cse_alum_roles
from data.testimonial import testimonial, testimonial_length
from data.hackathon_timeline import hackathon_timeline, hackathon_timeline_length
from data.alumni_timeline import alumni_timeline, alumni_timeline_length
from data.evaluation import overall_evaluation_rating, evaluation, count_evaluation_reports, count_evaluation_courses, evaluation_bridging, count_evaluation_bridging_courses, count_evaluation_bridging_reports
from data.best_comments import best_comments

# count
count_testimonial = testimonial_length
count_hackathon = hackathon_timeline_length
count_alumni = alumni_timeline_length
count_evaluation = count_evaluation_reports + count_evaluation_bridging_reports



environment = Environment(loader=FileSystemLoader("templates/"))

template = environment.get_template("index.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    office_room=office_room,
    office_sub=office_sub,
    office_url=office_url,
    
    count_testimonial=count_testimonial,
    count_hackathon=count_hackathon,
    count_alumni=count_alumni,
    count_evaluation = count_evaluation,
    social=social,
    slideshow=slideshow,
    )
with open("docs/index.html", "w") as f:
  f.write(content)


template = environment.get_template("profile.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    office_room=office_room,
    office_sub=office_sub,
    office_url=office_url,
    
    profile_description=profile_description,
    profile_roles=profile_roles,
    profile_url=profile_url,
    academic_title=academic_title,
    academic=academic,
    academic_length=academic_length,
    educator_title=educator_title, educator=educator, educator_length=educator_length,
    teaching_awards_title=teaching_awards_title, teaching_awards=teaching_awards, teaching_awards_length=teaching_awards_length,
    hackathon_roles_title=hackathon_roles_title, hackathon_roles=hackathon_roles, hackathon_roles_length=hackathon_roles_length,
    hackathon_awards_title=hackathon_awards_title, hackathon_awards=hackathon_awards, hackathon_awards_length=hackathon_awards_length,
    volunteer_roles_title=volunteer_roles_title, volunteer_roles=volunteer_roles, volunteer_roles_length=volunteer_roles_length,
    cyberport_alum_title=cyberport_alum_title, cyberport_alum_roles=cyberport_alum_roles,
    cse_alum_title=cse_alum_title, cse_alum_roles=cse_alum_roles
    )
with open("docs/profile/index.html", "w") as f:
  f.write(content)


template = environment.get_template("testimonial.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    testimonial=testimonial,
    testimonial_length=testimonial_length
)
with open("docs/testimonial/index.html", "w") as f:
  f.write(content)



template = environment.get_template("hackathon.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    hackathon_timeline=hackathon_timeline,
    hackathon_timeline_length=hackathon_timeline_length
)
with open("docs/hackathon/index.html", "w") as f:
  f.write(content)


template = environment.get_template("alumni.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    alumni_timeline=alumni_timeline,
    alumni_timeline_length=alumni_timeline_length
)
with open("docs/alumni/index.html", "w") as f:
  f.write(content)



template = environment.get_template("teaching.html")
content = template.render(
    baseURL=baseURL,
    homepage_text=homepage_text, 
    navbar_text=navbar_text,
    navbar_icon=navbar_icon,
    navbar_menu=navbar_menu,
    author=author, 
    email=email,
    job_title=job_title,
    keywords=keywords,
    overall_evaluation_rating=overall_evaluation_rating,
    best_comments=best_comments,
    count_evaluation_reports=count_evaluation_reports,
    count_evaluation_courses=count_evaluation_courses,
    evaluation=evaluation,
    evaluation_bridging=evaluation_bridging, 
    count_evaluation_bridging_courses=count_evaluation_bridging_courses, 
    count_evaluation_bridging_reports=count_evaluation_bridging_reports
)
with open("docs/teaching/index.html", "w") as f:
  f.write(content)
