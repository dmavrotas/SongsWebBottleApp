% rebase('layout.tpl')

<html>
<body>
    <h2>View Artist Results</h2>
    <table width="80%" height="50%" border='0' align="center">
        <th>National ID</th>
        <th>Name</th>
        <th>Surname</th>
        <th>Birth Year</th>
        %for row in rows:
        <tr>
            %for col in row:
            <td>{{col}}</td>
            %end
        </tr>
        %end
    </table>
</body>
</html>
