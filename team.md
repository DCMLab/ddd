---
title: Team
layout: page
published: true
nav_order: 5

---

# Team Members
{: .fs-9 }

Meet the team behind the project
{: .fs-6 .fw-300 }

---

<style>
 .grid {
  display: flex;
 }
.col-1-2 {
  flex: 1;
}

.uni {
  margin-bottom: 50px;
}

.cole-1-2:last-child {
  margin-left: 20px;
}
</style>

​This project requires domain expertise in various academic disciplines: music theory and
historical musicology on the one hand, computer/data science, and natural language processing. The
inherently interdisciplinary nature of the project thus posits it in the center of Digital Humanities research.

<div class="grid">
    <div class="col-1-2">
       <div class="content">
           <p>
           {% for member in site.data.team_members.team-left %}
           <img src="{{ site.url }}{{ site.baseurl }}/assets/images/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
           <h4>{{ member.name }}</h4>
           <i>{{ member.info }}</i>
            <div class="uni">
            {{ member.uni }}
            </div>
           {% endfor %}
           </p>
       </div>
    </div>
    <div class="col-1-2">
       <div class="content">
           <p>
           {% for member in site.data.team_members.team-right %}
           <img src="{{ site.url }}{{ site.baseurl }}/assets/images/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
           <h4>{{ member.name }}</h4>
           <i>{{ member.info }}</i>
            <div class="uni">
            {{ member.uni }}
            </div>
           {% endfor %}</p>
       </div>
    </div>
</div>