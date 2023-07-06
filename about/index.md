---
title: About
nav:
  order: 1
---

# About

We are a small group of dedicated software developers with the [Department of Biomedical Informatics](https://medschool.cuanschutz.edu/dbmi) at the [University of Colorado Anschutz](https://www.cuanschutz.edu/).
We support the labs, faculty, and staff within the Department, as well as external groups via collaboration.

## What we do

Our primary focus is creating high quality software and maintaining existing software.
We have a diverse team with a wide range of experience and expertise in software projects related to data-science, biology, medicine, statistics, and machine learning.

We can take a lab's ideas and scientific work, and turn them into a fully-realized, complete package of software, for both experts and lay-persons alike, that enables exploration of data, dissemination of knowledge, collaboration, advanced analyses, new insights, or lots more you could imagine.

Some of the things we do are:

- Modern, responsive web applications for data scientists, biologists, and more
- Powerful and flexible backend systems and APIs for programmers
- Interactive data visualizations for insight and engagement
- Research and mockups for rapid iteration and to ensure value before developing
- Efficient and reproducible pipelines for analyzing large data
- Scalable and robust cloud infrastructure
- Beautiful websites with cohesive branding and graphics
- Automations for processing, deployment, testing, monitoring, etc. that can save time, money, and hassle
- Code reviews for ensuring reliability, maintainability, and best practices
- Advising on software-related grant writing
- Software-focused technical support
- Workshops, training, teaching, etc.

But the best way to understand the things we do is by looking at the code and using the software yourself:

{%
  include button.html
  link="portfolio"
  text="Our portfolio"
  icon="fas fa-arrow-right"
  flip=true
  style="button"
%}

{% include section.html %}

## Teaching and communication

Whenever we can, we like to share our knowledge and skills to others.
We believe this benefits the community we operate in and allows us to create better software together.

On this website, we have a [blog](../blog) where we occasionally post tips, tricks, and other insights related to Git, workflows, code quality, and more.

We have given workshops and personalized lessons related to Docker, cloud services, and more.
We're always happy to set up a session to discuss technical trade whenever someone has the need.

## Scope of our work

Being central to the department, and not strictly associated with any particular lab or group within it, we need to ensure that we divide up our time and effort fairly.
While we can do things like build full-stack apps from scratch and maintain complex infrastructure, the projects we take on tend to be small to medium size so that we leave ourselves available to others who need our help.
Certain projects that are very large and long term in scope, such as ones that need to be HIPAA compliant, will fall outside of our purview and might lead you to hire a dedicated developer to fill your needs.
That said, we can still provide partial support as a consulting body, a repository of information, a hiring advisor, and more.

## Contact

We are working on a more formal way to submit requests for support, but in the meantime, please contact [Audrey Wen](mailto:audrey.wen@cuanschutz.edu) as an entrypoint for requesting work from the Software Engineering Team.

For general questions or technical help, we also have weekly open-office hours, Thursdays at 2:00 PM Mountain Time in the following Zoom room.
Feel free to stop by!

<script>
document.currentScript.insertAdjacentHTML(
  "beforebegin",
  `<a href="&#104;&#116;&#116;&#112;&#115;&#58;&#47;&#47;&#117;&#99;&#100;&#101;&#110;&#118;&#101;&#114;&#46;&#122;&#111;&#111;&#109;&#46;&#117;&#115;&#47;&#106;&#47;&#57;&#52;&#49;&#56;&#55;&#53;&#48;&#52;&#49;&#48;&#48;" target="_blank">Open office hours Zoom room</a>`
)
</script>

<!--
function encode(string) {
   return string
    .split("")
    .map((char) => `&#${char.charCodeAt(0)};`)
    .join("");
}
-->

## The Team

{% include list.html data="members" component="portrait" %}
