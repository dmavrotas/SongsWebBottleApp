% rebase('layout.tpl')

<html>
<body>
    <h2>Presentation of Songs</h2>
    <form action="/songs" method="get"/>
    <table width="50%" height="100%" border='0' align="center">
        <tr>
            <td>Song Title:</td>
            <td> <input id="titleid" type="text" class="toNavigate" name="title" /> </td>
        </tr>
        <tr>
            <td>Production Year:</td>
            <td> <input id="prodyearid" type="text" class="toNavigate" name="prodyear" /> </td>
        </tr>
        <tr>
            <td>Company:</td>
            <td> <input id="compid" type="text" class="toNavigate" name="company" /> </td>
        </tr>
    </table>
    <br/>
    <br/>
    <div style="text-align:center">
        <input type="submit" name="submitNew" value="Submit"/>
    </div>
</body>
</html>
