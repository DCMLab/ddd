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
  width: 33%;
}

.uni {
  margin-bottom: 50px;
}

.cole-1-2:last-child {
  margin-left: 20px;
}

.team-img {
  display: block;
}

.grid h4 > span {
  font-weight: 900;
}

.back img {
  filter: brightness(0%);
}

/* entire container, keeps perspective */
.flip-container {
	perspective: 1000px;
}
	/* flip the pane when hovered */
	.flip-container:hover .flipper, .flip-container.hover .flipper {
		transform: rotateY(180deg);
	}

.flip-container, .front, .back {
	height: 170px;
  width:170px;
}

/* flip speed goes here */
.flipper {
	transition: 0.4s;
  transform-style: preserve-3d;
	position: relative;
}

/* hide back of pane during swap */
.front, .back {
	backface-visibility: hidden;
	position: absolute;
	top: 0;
	left: 0;
}

/* front pane, placed above back */
.front {
	z-index: 2;
	/* for firefox 31 */
	transform: rotateY(0deg);
}

/* back, initially hidden pane */
.back {
	transform: rotateY(180deg);
  background-color: lightgrey;
  border-radius: 5px;
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
           <div class="flip-container">
           <div class="flipper">
           <div class="front">
           <img src="{{ site.url }}{{ site.baseurl }}/assets/images/{{ member.photo }}" class="team-img" width="70%" />
           </div>
           <div class="back">
           <h4>What about a title here?</h4>
           <p>Optional text, icons or social links or extra informations.</p>
           </div>
           </div>
           </div>
           <h4>{{ member.name1 }}<span> {{ member.name2 }}</span></h4>
           <i>{{ member.info }}</i>
            <div class="uni">
            {{ member.uni }}
            </div>
           {% endfor %}</p>
       </div>
    </div>
    <div class="col-1-2">
       <div class="content">
           <p>
           {% for member in site.data.team_members.team-middle %}
           <img src="{{ site.url }}{{ site.baseurl }}/assets/images/{{ member.photo }}" class="team-img" width="70%" />
           <h4>{{ member.name1 }}<span> {{ member.name2 }}</span></h4>
           <i>{{ member.info }}</i>
            <div class="uni">
            {{ member.uni }}
            </div>
           {% endfor %}</p>
       </div>
    </div>
    <div class="col-1-2">
       <div class="content">
           <p>
           {% for member in site.data.team_members.team-right %}
           <img src="{{ site.url }}{{ site.baseurl }}/assets/images/{{ member.photo }}" class="team-img" width="70%" />
           <h4>{{ member.name1 }}<span> {{ member.name2 }}</span></h4>
           <i>{{ member.info }}</i>
            <div class="uni">
            {{ member.uni }}
            </div>
           {% endfor %}</p>
       </div>
    </div>
</div>