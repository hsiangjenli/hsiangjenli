<table>

<tr>
    <td>Host</td>
    <td>Year</td>
    <td>Competition Name</td>
    <td>Ranking</td>
</tr>

{% for award in awards %}

<tr>
    <td> <img width='40px' src="{{ awards[award]['Cover'] }}"> </td>
    <td> {{ awards[award]['Year'] }} </td>
    <td> <b> {{ awards[award]['Name']['Host'] }} </b><br>{{ awards[award]['Name']['English'] }} </td>
    <td> {{ awards[award]['Ranking'] }} </td>

</tr>


{% endfor %}

</table>