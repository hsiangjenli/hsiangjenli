<table>
{% for edu in educations %}
    {% set edu_logo = is_abs_url( educations[edu]['university']['basic_info']['image'], static ) %}
<tr>
    <td>
        <img align="center" width='40px' style='min-width: 40px' src="{{ edu_logo }}">
    </td>
    <td>
        {{ educations[edu]['university']['basic_info']['graduate_year'] }}
    </td>
    <td>
        <b>{{ educations[edu]['university'][language]['name'] }}</b>, {{ educations[edu]['university'][language]['country'] }} <br>
        {{ edu }} in {{ educations[edu]['university'][language]['major'] }}
    </td>
    <td>{{ educations[edu]['university'][language]['description'] }}</td>
</tr>

{% endfor %}
</table>