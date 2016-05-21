% rebase('layout.tpl')

<html>
<body>
    <h2>Insert Artist</h2>
    <form action="/insertartist" method="get"/>
    <table width="50%" height="100%" border='0' align="center">
        <tr>
            <td>National ID:</td>
            <td> <input id="nameid" type="text" class="toNavigate" name="natid" /> </td>
        </tr>
        <tr>
            <td>Name:</td>
            <td> <input id="surnameid" type="text" class="toNavigate" name="name" /> </td>
        </tr>
        <tr>
            <td>Surname:</td>
            <td> <input id="bdfid" type="text" class="toNavigate" name="surname" /> </td>
        </tr>
        <tr>
            <td>Birth Year:</td>
            <td> <input id="bdtid" type="text" class="toNavigate" name="byear" /> </td>
        </tr>
    </table>
    <br/>
    <br/>
    <div style="text-align:center">
        <input type="submit" name="submitNew" value="Submit"/>
    </div>
</body>
</html>
