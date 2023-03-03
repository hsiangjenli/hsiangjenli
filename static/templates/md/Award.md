<table>

<tr>
    <td><b>Host</b></td>
    <td><b>Year</b></td>
    <td><b>Competition Name</b></td>
    <td><b>Ranking</b></td>
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