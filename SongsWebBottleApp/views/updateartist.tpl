% rebase('layout.tpl')

<html>
<body>
    <h2>Update Artist Information</h2>
    <form action="/updateartist" method="get"/>
    <table width="50%" height="100%" border='0' align="center">
        <tr>
            <td>Name:</td>
            <td> <input id="surnameid" type="text" class="toNavigate" name="name" value="{{name}}"/> </td>
        </tr>
        <tr>
            <td>Surname:</td>
            <td> <input id="bdfid" type="text" class="toNavigate" name="surname" value="{{surname}}"/> </td>
        </tr>
        <tr>
            <td>Birth Year:</td>
            <td> <input id="bdtid" type="text" class="toNavigate" name="byear" value="{{byear}}"/> </td>
        </tr>
    </table>
    <br/>
    <br/>
    <div style="text-align:center">
        <button type="submit" name="submitNew" value="{{id}}">Update Information</button>
    </div>
</body>
</html>
