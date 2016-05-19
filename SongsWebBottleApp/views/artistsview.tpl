% rebase('layout.tpl', title=title, year=year)

<html>
<head>
    <title>Presentation of Artists</title>
</head>
<body>
    <table width="100%" height="100%" border='0' align="center">
        <tr>
            <td>
                <h2>Presentation of Artists</h2>
                <form>
                    Name: <input type="text" class="toSubmit" name="name" /><br />
                    Surname: <input type="text" class="toSubmit" name="surname" /><br />
                    Birth Year - From: <input type="text" class="toSubmit" name="byfrom" /><br />
                    Birth Year - To: <input type="text" class="toSubmit" name="byto" /><br />
                    <select id="artisttypes">
                        <option value="1">Singer</option>
                        <option value="2">Song Writer</option>
                        <option value="3">Composer</option>
                    </select> <br />
                    <input type="button" name="button" value="Submit" onClick="submitForm(this.form, 'insertData')" /> 
                </form>
            </td>
        </tr>
    </table>
</body>
</html>
