from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


testimonials = [
        {
            "name": "Atish Banerjea",
            "job": "Chief Information Officer",
            "quote": "We share a great responsibility in shaping the future",
            "img": "/static/img/atish.png"
        },
        {
            "name": "Qi Z.",
            "job": "Manager, Developer Operations",
            "quote": "We are solution-seekers and bold builders.",
            "img": "/static/img/qi.png"
        },
        {
            "name": "Nishita A.",
            "job": "Software Engineering Manager",
            "quote": "To be a successful engineer, empathy is key.",
            "img": "/static/img/nishita.png"
        },
        {
            "name": "Arun Chandra",
            "job": "VP, Scaled Operations",
            "quote": "We start from a position of putting people first.",
            "img": "/static/img/arun.png"
        },
        {
            "name": "Limor Z.",
            "job": "Engineering Manager",
            "quote": "People's lives change once they're able to connect.",
            "img": "/static/img/limor.png"
        },
        {
            "name": "Adriana V.",
            "job": "Software Engineer",
            "quote": "Learn something new; there's nothing stopping you.",
            "img": "/static/img/adriana.png"
        },
]


openjobs = [
    {
        "title": "Software Engineer",
        "type": "Full Time",
        "location": "New York, NY",
        "desc": "Software engineers apply engineering principles and knowledge of programming languages to build software solutions for end users",
        "salary": "$100,000 - $150,000",
        "logo": "fa-facebook",
        "id": "fb"
    },
    {
        "title": "Frontend Developer",
        "type": "Internship",
        "location": "San Jose, CA",
        "desc": "A front-end developer architects and develops websites and applications using web technologies (i.e., HTML, CSS, DOM, and JavaScript)",
        "salary": "$50,000 - $75,000",
        "logo": "fa-facebook-messenger",
        "id": "mg"
    },
    {
        "title": "Backend Engineer",
        "type": "Part Time",
        "location": "Chicago, IL",
        "desc": "A backend engineer is responsible for designing, building, and maintaining the server-side of web applications",
        "salary": "$125,000 - $175,000",
        "logo": "fa-whatsapp",
        "id": "wa"
    },
    {
        "title": "Marketing Agent",
        "type": "Contract",
        "location": "Remote",
        "desc": "A marketing agent works to match a company with a media outlet like a radio or TV station, social media page, or website to advertise a product or service",
        "salary": "$20,000 - $40,000",
        "logo": "fa-instagram",
        "id": "ig"
    },
    {
        "title": "UI/UX Designer",
        "type": "Full Time",
        "location": "Remote",
        "desc": "UI designers design all the screens that make up a digital user interface, as well as the individual elements featured on those screens",
        "salary": "$100,000 - $125,000",
        "logo": "fa-instagram",
        "id": "ig"
    },
    {
        "title": "Business Analyst",
        "type": "Full Time",
        "location": "Seattle, WA",
        "desc": "Business analysts use data to form business insights and recommend changes in businesses and other organizations",
        "salary": "$150,000 - $175,000",
        "logo": "fa-whatsapp",
        "id": "wa"
    },
]

topJob = {
    "title": "Chief Executive Officer",
    "type": "Full Time",
    "location": "Menlo Park, CA",
    "desc": "This is it! The big position is now open for anyone to apply for. Since Big Daddy Mark left us, we have been looking for someone to replace him. Do you have what it takes to lead Meta to new heights? If so, then apply today!",
    "salary": "$900,000 - $1,000,000",
    "logo": "fa-facebook",
    "id": "fb"
}


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', testimonials=testimonials)


@app.route('/jobs')
def jobs():
    return render_template('jobs.html', openjobs=openjobs, topJob=topJob)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)