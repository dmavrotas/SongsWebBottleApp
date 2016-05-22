% rebase('layout.tpl')

<html>
<body>
    <h2>View Artist Results</h2>
    <form action="/artistsview" method="get" />
    <table width="80%" height="50%" border='0' align="center">
        <th>National ID</th>
        <th>Name</th>
        <th>Surname</th>
        <th>Birth Year</th>
        <th>Edit</th>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
            <td><button type="submit" name="edit" value="{{row[0]}}" >Edit</button></td>
        </tr>
        %end
    </table>
</body>
</html>
