---
title: Team
layout: page
published: true
nav_order: 5

---

# Meet the team behind the project
{: .fs-9 }

{: .fs-6 .fw-300 }

---

<style>
  #lastname {
    font-weight: 700;
  }
</style>

​This project requires domain expertise in various academic disciplines: music theory and
historical musicology on the one hand, computer/data science, and natural language processing. The
inherently interdisciplinary nature of the project thus posits it in the center of Digital Humanities research.

{% for member in site.data.team_members.team %}
  <h4>{{ member.name1 }}<span id="lastname"> {{ member.name2 }}</span></h4>
  {{ member.info }}
{% endfor %}
