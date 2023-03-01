{% for edu in educations %}
**{{ educations[edu]['University']['Name'] }}**, {{ educations[edu]['University']['Country'] }}  
{{ edu }} in {{ educations[edu]['Major']['Name'] }}

{% endfor %}