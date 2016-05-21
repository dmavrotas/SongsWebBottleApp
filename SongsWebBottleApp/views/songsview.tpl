% rebase('layout.tpl')

<html>
<body>
    <h2>View Songs Results</h2>
    <table width="80%" height="50%" border='0' align="center">
        <th>Title</th>
        <th>Composer</th>
        <th>Songwriter</th>
        <th>Production Year</th>
        <th>Company</th>
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
