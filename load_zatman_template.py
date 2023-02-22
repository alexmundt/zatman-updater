

def insert_into_html(text):
    string = \
f"""
<!DOCTYPE html>

<html>

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" href="include/main_style.css"/>
    <title>SEDI Group</title>
    <link rel="icon" href="images/favicon-16x16.png" type="image/png" sizes="16x16">
</head>

<body>

    <div class="body_left body_left_width">
            </div>
    <div class="body_right body_right_width">
            </div>

    <div class="body_main body_main_width" >

        <div id="banner" name="banner" ><br>

            <div id="banner_title" name="banner_title">
                <title1>SEDI</title1><br>
                <title2>Study of the Earth's Deep Interior,
                    <br> a Committee of IUGG</title2>

            </div>

            <div id="logo" name="logo">
                <img src="./images/IOGGlogo.png" height="120" width="130">
            </div>
            <div id="sedilogo" name="sedilogo">
                    <img src="./images/sedilogo.png" height="120" width="130">
            </div>



            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <div id="banner_bottom" name="banner_bottom"
                class="non_sticky_banner">
                <div id="vertical_menu" name="vertical_menu">
                    <ul id="vertical_ul">
                        <li class="vertical_li"> <a class="topactive" href="./introduction.html">Home</a> </li>
                        <li class="vertical_li"> <a href="./nextmeeting.html">Next SEDI Meeting</a> </li>
                        <li class="vertical_li"> <a href="./papers.html">SEDI Related Papers</a> </li>
                        <li class="vertical_li"> <a href="./jobs.html">Job Postings</a> </li>
                    </ul>
                </div>
            </div>




        </div>







        <div id="menu" name="menu" class="menu" >
            <ul id="side_ul">
                <li><a href="./introduction.html">Introduction to Sedi </a></li>
                <li><a href="./admin.html">Structure, Administration and Membership </a></li>
                <li><a href="./symposia.html">Symposia and Meetings </a></li>
                <li><a href="./dialog.html">Archive of the Deep Earth Dialog</a></li>
                <li><a href="./activities.html">National Activities and SEDI related links </a></li>
                <li><a href="./doornbos.html">Doornbos Prizewinners </a></li>
                <li><a href="./zatman.html"class="active"> Zatman Lectures</a></li>
                <li><a href="./conduct.html"> Code of Conduct</a></li>
            </ul>
        </div>
        <div id="content" name="content">

<c_header>Zatman Lectures</c_header>
<br>

<p>The Zatman lecture is
given at each biennial SEDI meeting by a prominent young scientist who has done
outstanding work on core dynamics. Stephen Zatman was
himself a prominent young scientist who studied core dynamics, and whose life
was tragically cut short. </p>

<p align="center">
<div style="overflow-x:auto;">
<table id = "zatman_table">

    <tr>
    <th>Year</th>
    <th>Lecturer</th>
    <th>Title</th>
    </tr>

    {text}

</table>

</div>
        </div>


    </div >

    <script src="./include/script.js"></script>


    </body>
</html>

"""
    return string
