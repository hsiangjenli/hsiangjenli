{% for edu in educations %}
**<h3>{{ educations[edu]['University']['Name'] }}**, {{ educations[edu]['University']['Country'] }}</h3>  
{{ edu }} in {{ educations[edu]['Major']['Name'] }}

{% endfor %}